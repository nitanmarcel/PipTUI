import curses

from npyscreen import FormBaseNew


class FormBaseNewHinted(FormBaseNew):
    def display_menu_advert_at(self):
        return self.lines - 1, 1

    def draw_form(self):
        super(FormBaseNewHinted, self).draw_form()
        menu_advert = '^A: Install\t\t^R: Uninstall\t\t^U: Update\t\t^O: Open in Browser\t\t^H: Open HomePage\t\t^Q: Quit'
        if isinstance(menu_advert, bytes):
            menu_advert = menu_advert.decode('utf-8', 'replace')
        y, x = self.display_menu_advert_at()
        self.add_line(y, x,
                      menu_advert,
                      self.make_attributes_list(menu_advert, curses.A_NORMAL),
                      self.columns - x - 1
                      )
