class EnvironmentUtil:

    def __init__(self):
        self.gui_upload_portal = ''

    def dev_environment_variables(self):
        self.gui_upload_portal = 'https://www.masoko.com/sign-in'
        return self.gui_upload_portal

    def stage_environment_variables(self):
        self.gui_upload_portal = 'https://www.masoko.com/sign-in'
        return self.gui_upload_portal

    def prod_environment_variables(self):
        self.gui_upload_portal = 'https://www.masoko.com/sign-in'
        return self.gui_upload_portal



