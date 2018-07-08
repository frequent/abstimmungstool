# -*- coding: utf-8 -*-
# ==============================================================================
# Voty initadmin views/actions
# ==============================================================================
#
# parameters (*default)
# ------------------------------------------------------------------------------

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_POST
from django.contrib.sites.models import Site
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib import messages
from django.conf import settings
from django.utils.translation import ugettext as _

import account.views
from account.models import SignupCodeResult, SignupCode

from .models import InviteBatch
from .forms import UploadFileForm, LoginEmailOrUsernameForm, UserEditForm

from datetime import datetime, timedelta
from uuid import uuid4
from io import StringIO, TextIOWrapper
import csv


def invite_single_user(first_name, last_name, email, site):
  
  # find already invited users by existing signup codes    
  try:
    code = SignupCode.objects.get(email=email)
  except SignupCode.DoesNotExist:
    code = SignupCode(
      email=email,
      code=uuid4().hex[:20],
      max_uses=1,
      sent=datetime.utcnow(),
      expiry=datetime.utcnow() + timedelta(days=14)
    )
    newly_added += 1
    code.save()

    EmailMessage(
      render_to_string("initadmin/email_invite_subject.txt"),
      render_to_string(
        "initadmin/email_invite_message.txt",
        context=dict(
          domain=site.domain,
          code=code,
          first_name=first_name
        )
      ),
      settings.DEFAULT_FROM_EMAIL,
      [email]
    ).send()

  return code

def invite_batch_users(file):
  site = Site.objects.get_current()
  total = newly_added = 0
  reader = csv.DictReader(file, delimiter=";")
  results = StringIO()
  writer = csv.DictWriter(results, fieldnames=["first_name", "last_name", "email_address", "invite_code"])

  writer.writeheader()

  for item in reader:
    total += 1
    email = item["email_address"]
    first_name = item["first_name"]
    last_name = item["last_name"]

    sent_with_code = invite_single_user(first_name, last_name, email, site)

    writer.writerow({
      "first_name": first_name,
      "last_name": last_name,
      "email_address": email,
      "invite_code": sent_with_code.code
    })

    InviteBatch(
      payload=results.getvalue(),
      total_found=total,
      new_added=newly_added
    ).save()

    return total, newly_added


def is_in_multiple_groups(user):
    return user.groups.filter(name__in=['Policy Team Member', 'Policy Team Lead']).exists()


#
# ____    ____  __   ___________    __    ____   _______.
# \   \  /   / |  | |   ____\   \  /  \  /   /  /       |
#  \   \/   /  |  | |  |__   \   \/    \/   /  |   (----`
#   \      /   |  | |   __|   \            /    \   \    
#    \    /    |  | |  |____   \    /\    / .----)   |   
#     \__/     |__| |_______|   \__/  \__/  |_______/    
#
#                                                       

# ---------------------------- LoginView ---------------------------------------
# XXX why is it a class? can't this be just a form?
class LoginView(account.views.LoginView):
  form_class = LoginEmailOrUsernameForm

# ---------------------------- User List  --------------------------------------
def user_list(request):
  return render(request, "Hello User List", context={})

# -------------------------- Initiative List  ----------------------------------
def initiative_list(request):
  return render(request, "Hello Initiative List", context={})

# -------------------------- Profile Localise ----------------------------------
def profile_localise(request):
  return render(request, "Hello Localise Profile", context={})

# --------------------------- Profile Edit -------------------------------------
@login_required
def profile_edit(request):
  user = get_object_or_404(get_user_model(), pk=request.user.id)
  if request.method == "POST":
    form = UserEditForm(request.POST, instance=user)
    if form.save():
      messages.success(request, _("Data updated."))
  else:
    form = UserEditForm(instance=user)

  return render(request, "initadmin/profile_edit.html", context=dict(form=form))

# --------------------------- Profile Delete -----------------------------------
def profile_delete(request):
    return render(request, "Hello Profile Delete", context={})

# download imported files
#@login_required
#@user_passes_test(lambda u: is_in_multiple_groups(u))
#def download_csv(request, id):
#    batch = get_object_or_404(InviteBatch, pk=id)
#    response = HttpResponse(batch.payload, content_type='text/csv')
#    response['Content-Disposition'] = 'attachment; filename=invited_users.csv'
#    return response

# --------------------------- Invite Users -------------------------------------
@login_required
@user_passes_test(lambda u: is_in_multiple_groups(u))
def user_invite(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            total, send = invite_batch_users(TextIOWrapper(request.FILES['file'].file, encoding=request.encoding))
            messages.success(request, "".join(["{}/{}".format(send, total), _("invitations were sent")]))
    else:
        form = UploadFileForm()
    return render(request, 'initadmin/invite_users.html', context=dict(form=form,
        invitebatches=InviteBatch.objects.order_by("-created_at")))

# active users (recently logged in first)
#@login_required
#@user_passes_test(lambda u: is_in_multiple_groups(u))
#def active_users(request):
#    users_q = get_user_model().objects.filter(is_active=True, avatar__primary=True).order_by("-last_login")
#    return render(request, "initadmin/active_users.html", dict(users=users_q))


