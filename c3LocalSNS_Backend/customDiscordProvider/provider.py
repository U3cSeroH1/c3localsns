from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider
from allauth.account.signals import user_signed_up, user_logged_in
from django.http.response import HttpResponseForbidden
from django.conf import settings
from logging import getLogger
from allauth.socialaccount.models import SocialAccount, SocialToken
from .discord_cli import checkGuild, getGuilds
from django.conf import settings

logger = getLogger('Django')


class DiscordAccount(ProviderAccount):
    def to_str(self):
        dflt = super(DiscordAccount, self).to_str()
        return self.account.extra_data.get('username', dflt)


class DiscordProvider(OAuth2Provider):
    id = 'discord'
    name = 'Discord'
    account_class = DiscordAccount

    def extract_uid(self, data):
        return str(data['id'])

    def extract_common_fields(self, data):
        return dict(
            email=data.get('email'),
            username=data.get('username'),
            name=data.get('username'),
        )

    def get_default_scope(self):
        # ここを変更することでsettingから読み込めるようにする
        return settings.DISCORD_SCOPES


provider_classes = [DiscordProvider]

def checkUserInDiscordGuild(user, **kwargs):
    logger.debug(user)
    socialAccount = SocialAccount.objects.filter(user=user).first()
    socialToken = SocialToken.objects.filter(account=socialAccount).first()
    logger.debug(socialToken.token)
    try:
        if not checkGuild(socialToken.token, settings.GUILD_ID):
            logger.debug(status)
            raise HttpResponseForbidden()
    except BaseException:
        raise HttpResponseForbidden()

user_logged_in.connect(checkUserInDiscordGuild)