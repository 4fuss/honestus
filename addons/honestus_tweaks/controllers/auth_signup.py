from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.http import request


class HonestusAuthSignupHome(AuthSignupHome):
    """Override AuthSignupHome methods to accept `mobile` parameter."""

    def get_auth_signup_qcontext(self):
        """Add `mobile` to `qcontext`."""
        super_qcontext = super().get_auth_signup_qcontext()
        qcontext = {
            k: v
            for (k, v)
            in request.params.items()
            if k in ['mobile']
        }
        super_qcontext.update(qcontext)
        return super_qcontext

    def _prepare_signup_values(self, qcontext):
        """Add `mobile` to res.partner create values."""
        super_values = super()._prepare_signup_values(qcontext)
        values = {k: qcontext.get(k) for k in ['mobile']}
        super_values.update(values)
        return super_values
