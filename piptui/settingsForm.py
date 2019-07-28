from npyscreen import ActionForm, OptionList, TitleText, OptionListDisplay, OptionSingleChoice
from .settings import set_config_value, get_config_value, THEME_FOLDER
import os


class ChangeUserOption(OptionSingleChoice):
    def when_set(self):
        if len(self.value[0]) > 1:
            set_config_value('use_user_arg', list(self.value)[0])
            self.value = self.value[0]


class ChangeUpdateOption(OptionSingleChoice):
    def when_set(self):
        if len(self.value[0]) > 1:
            set_config_value('check_for_update', list(self.value)[0])
            self.value = self.value[0]


class ChangeThemeOption(OptionSingleChoice):
    def when_set(self):
        if len(self.value[0]) > 1:
            set_config_value('theme', list(self.value)[0])
            self.value = self.value[0]


class SettingsForm(ActionForm):
    def create(self):
        self.name = 'Settings'
        option = OptionList()
        options = option.options
        options.append(
            ChangeUserOption(
                'Install as user?',
                value=get_config_value('use_user_arg'),
                choices=[
                    'true',
                    'false'],
                documentation=['Disable or enable pip\'s \'--user\' command argument']))
        options.append(
            ChangeUpdateOption(
                'Check For App Update?',
                value=get_config_value('check_for_update'),
                choices=[
                    'true',
                    'false'],
                documentation=['Disable or enable application update check at startup']))
        options.append(
            ChangeThemeOption(
                'Theme:',
                value=get_config_value('theme'),
                choices=os.listdir(THEME_FOLDER),
                documentation=['Change app\'s theme']))
        self.add(OptionListDisplay, values=options)

    def on_ok(self):
        self.parentApp.switchForm('MAIN')

    def on_cancel(self):
        self.parentApp.switchForm('MAIN')
