import sys
import os
# import xlrd
import zipfile
import base64


class ExcelImgRead(object):

    def change_file_name(self, file_path, old_name, new_type = '.zip'):
        """
        修改指定目录下的文件类型名
        :param file_path:
        :param old:
        :param new:
        :return:
        """
        old_path = os.path.join(file_path, old_name)
        if not os.path.exists(old_path):
            print ('No such File! :%s' % old_path)
            return False
        new_name = str(old_name.split('.')[0]) + new_type
        new_path = os.path.join(file_path, new_name)
        if os.path.exists(new_path):
            os.remove(new_path)
        os.rename(old_path, new_path)

    def unzip_file(self, file_path):
        """
        解压缩指定目录下的Zip文件
        :param file_path:
        :return:
        """
        # pic_paths = []
        pic_dir = 'xl/media'
        file_list = os.listdir(file_path)
        for file_name in file_list:
            if file_name.split('.')[1] == 'zip':
                file_zip = zipfile.ZipFile(os.path.join(file_path, file_name), 'r')
                zipdir = file_name.split('.')[0]
                for files in file_zip.namelist():
                    file_zip.extract(files, os.path.join(file_path, zipdir))  # 解压到指定文件目录
                file_zip.close()
                pic_path = os.path.join(file_path, zipdir, pic_dir)
                # pic_paths.append(pic_path)
                return pic_path


    def excel_pic_read(self, file_path):
            """
            读取excel中的图片base64
            :param file_path:
            :param file_name:
            :return:图片的base64编码字符串
            """
            # for file_name in os.listdir(file_path):
            ExcelImgRead().change_file_name(file_path, file_name)
            return ExcelImgRead().unzip_file(file_path)


    def main(self):

        file_path = '/home/amark/workspace/excel1'
        return self.excel_pic_read(file_path)

if __name__ == '__main__':
    e = ExcelImgRead()
    res = e.main()
