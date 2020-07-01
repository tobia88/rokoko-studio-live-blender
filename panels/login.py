import bpy
from .main import ToolPanel, separator
from ..operators.login import LoginButton, ShowPassword
from ..core import login
from ..core.icon_manager import Icons


class LoginPanel(ToolPanel, bpy.types.Panel):
    bl_idname = 'VIEW3D_PT_rsl_login'
    bl_label = 'Login'

    def draw(self, context):
        layout = self.layout

        row = layout.row(align=True)
        row.label(text='Login with your Rokoko ID:', icon_value=Icons.STUDIO_LIVE_LOGO.get_icon())
        separator(layout, 0.1)

        row = layout.row(align=True)
        row.scale_y = 0.5
        row.label(text='Email:')
        row = layout.row(align=True)
        row.prop(context.scene, 'rsl_login_email', text='')

        separator(layout, 0.01)

        row = layout.row(align=True)
        row.scale_y = 0.5
        row.label(text='Password:')

        split = layout.row(align=True)
        row = split.row(align=True)
        row.prop(context.scene, 'rsl_login_password_shown' if login.show_password else 'rsl_login_password', text='')
        row = split.row(align=True)
        row.alignment = 'RIGHT'
        row.operator(ShowPassword.bl_idname, text="", icon='HIDE_OFF' if login.show_password else 'HIDE_ON')

        if login.show_wrong_auth:
            row = layout.row(align=True)
            row.label(text='Wrong email or password!', icon='ERROR')

        row = layout.row(align=True)
        row.operator(LoginButton.bl_idname, icon='X')
