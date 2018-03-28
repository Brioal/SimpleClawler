# encoding=utf-8
class Ouputer(object):
    def __init__(self):
        self.datas = []

    # 添加数据
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    # 输出html
    def out_put_html(self):
        fout= open('output.html','w')
        fout.write("<html>")
        fout.write("</body>")
        fout.write("<table>")
        for data in  self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>"%data['url'])
            fout.write("<td>%s</td>"%data['title'].encode('utf-8'))
            fout.write("<td>%s</td>"%data['summary'].encode('utf-8'))
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("<body>")
        fout.write("</html>")
        pass