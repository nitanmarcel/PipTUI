import curses

from npyscreen import FormBaseNew, ActionForm


class FormBaseNewHinted(FormBaseNew):
    FRAMED = False

    def display_menu_advert_at(self):
        return self.lines - 1, 1

    def draw_form(self):
        super(FormBaseNewHinted, self).draw_form()
        menu_advert = '^A: Install\t^R: Uninstall\t^U: Update\t^O: Open in Browser\t^H: Open HomePage\t^D: Details\t^Q: Quit'
        if isinstance(menu_advert, bytes):
            menu_advert = menu_advert.decode('utf-8', 'replace')
        y, x = self.display_menu_advert_at()
        self.add_line(y, x,
                      menu_advert,
                      self.make_attributes_list(menu_advert, curses.A_NORMAL),
                      self.columns - x - 1,
                      )


class ActionFormHinted(FormBaseNew):
    def display_menu_advert_at(self):
        return self.lines - 1, 1

    def draw_form(self):
        super(ActionFormHinted, self).draw_form()
        menu_advert = '^A: Install Release\t^Q: Home'
        if isinstance(menu_advert, bytes):
            menu_advert = menu_advert.decode('utf-8', 'replace')
        y, x = self.display_menu_advert_at()
        self.add_line(y, x,
                      menu_advert,
                      self.make_attributes_list(menu_advert, curses.A_NORMAL),
                      self.columns - x - 1,
                      )
