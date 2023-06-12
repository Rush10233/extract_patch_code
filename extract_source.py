from html.parser import HTMLParser


class ParseNavigation(HTMLParser):
    def __init__(self, *, convert_charrefs: bool = ...) -> None:
        self.source_list = []
        self.is_linkage = False
        self.cur_linkage = ""
        self.pre='https://gcc.gnu.org'
        self.patch_name=""
        self.decide_name=False
        super().__init__(convert_charrefs=convert_charrefs)

    def handle_starttag(self, tag: str, attrs) -> None:
        if tag == 'a' and len(attrs)>0 and attrs[0][0]=='class' and attrs[0][1]=='title':
            self.decide_name=True
        if tag == 'td' and len(attrs) > 0 and attrs[0][1] == 'link':
            self.is_linkage = True
        if self.is_linkage and tag == 'a' and len(attrs) > 0:
            c_url = attrs[0][1]
            if c_url.find('testsuite') == -1 and c_url.find('ChangeLog') == -1:
                self.cur_linkage = c_url
            else:
                self.is_linkage = False

    def handle_endtag(self, tag: str) -> None:
        self.is_linkage = False

    def handle_data(self, data: str) -> None:
        if self.decide_name:
            self.decide_name=False
            self.patch_name=data
        if self.is_linkage:
            if data == 'diff':
                self.source_list.append(self.pre+self.cur_linkage)

    def get_source(self):
        return self.source_list
    def get_patch_name(self):
        self.patch_name=self.patch_name.replace('/','_')
        self.patch_name=self.patch_name.replace('.','_')
        self.patch_name=self.patch_name.replace(':','_')
        return self.patch_name

