from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
import subprocess
import re
from colors import color
from numify import numify
import time
from pyhtmlapi import write_html, write_final_script
from subprocess import CREATE_NO_WINDOW
import glob

html_preferred = True
# ayeayemyint180
manual_update = ["", "", "",
                 "", "", "",
                 "", "", "",
                 "", "", "",
                 "", "", "",
                 "", "", "",
                 "", "", "",
                 "", "", "",
                 "", "", "",
                 "", "", "",
                 "", "", ""
                 ]

fast_update_flag = False
# fast_update_flag = True
if fast_update_flag:
    directories = fast_update
else:
    directories = manual_update
MAX_PAGE = 30
single_directory = True
view_count = False
singleDirectory = ""
last_name = ""
user_link_ = "https://www.tiktok.com/@" + singleDirectory
FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')

regex = "\d+_@(.+)_(\d+)"
path = "D://#Douyin//"
path_E = "E://#Douyin//"
path_Processing = "E://#Processing//"
path_d_cmpl = "D://#Douyin_Completed//"
path_d_process = "D://#Douyin_processing//"


class BreakIt(Exception):
    pass


def explore(path):
    path = os.path.normpath(path)

    if os.path.isdir(path):
        subprocess.run([FILEBROWSER_PATH, path])
    elif os.path.isfile(path):
        subprocess.run([FILEBROWSER_PATH, '/select,', path])


def log(lines, user):
    if not os.path.exists(path + "//outputs"):
        os.mkdir(path + "//outputs")
    opt_path = path + "//outputs//" + user + ".txt"
    f = open(opt_path, "a")
    f.writelines(lines)
    f.close()


if __name__ == '__main__':
    if os.path.exists("C://Users//USER//Desktop//Links.html"):
        x = input("Links.html already exists. Are you sure you want to overwrite?(y/n) : ")
        if x == 'y':
            os.remove("C://Users//USER//Desktop//Links.html")
        if x == 'n':
            print("Skipping ......")
    options = webdriver.ChromeOptions()
    # caps = DesiredCapabilities().CHROME
    # caps["pageLoadStrategy"] = "eager"
    # options.add_argument("--headless")
    options.add_extension(r'Link-Grabber.crx')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


    def scroll_to_bottom(driver):
        old_position = 0
        new_position = None
        local_count_page = 1
        while new_position != old_position:
            print("\rLoading page {} ...".format(local_count_page), end='', flush=True)
            # print("Loading page {} ...".format(local_count_page))
            for i in range(1, 7):
                old_position = driver.execute_script(
                    ("return (window.pageYOffset !== undefined) ?"
                     " window.pageYOffset : (document.documentElement ||"
                     " document.body.parentNode || document.body);"))
                time.sleep(1.5)
                driver.execute_script((
                    "var scrollingElement = (document.scrollingElement ||"
                    " document.body);scrollingElement.scrollTop ="
                    " scrollingElement.scrollHeight;"))
                new_position = driver.execute_script(
                    ("return (window.pageYOffset !== undefined) ?"
                     " window.pageYOffset : (document.documentElement ||"
                     " document.body.parentNode || document.body);"))
                if new_position == old_position:
                    time.sleep(4)
                else:
                    break
            local_count_page += 1


    def tiktok(DIR):
        names = []
        if os.path.exists(path + DIR):
            files = glob.glob(path + DIR + '/**/*.mp4', recursive=True)
            flag = 0
        elif os.path.exists(path_d_process + DIR):
            files = glob.glob(path_d_process + DIR + '/**/*.mp4', recursive=True)
            flag = 1
        elif os.path.exists(path_d_cmpl + DIR):
            files = glob.glob(path_d_cmpl + DIR + '/**/*.mp4', recursive=True)
            flag = 2
        elif os.path.exists(path_Processing + DIR):
            files = glob.glob(path_Processing + DIR + '/**/*.mp4', recursive=True)
            flag = 3
        else:
            files = glob.glob(path_E + DIR + '/**/*.mp4', recursive=True)
            flag = 4
        for file in files:
            filename = os.path.basename(file)
            if filename.startswith("_@"):
                pass
            else:
                names.append(filename)
        names.sort()
        if flag == 0:
            print("\n{} : {}".format(path + DIR, len(names)))
        if flag == 1:
            print("\n{} : {}".format(path_d_process + DIR, len(names)))
        if flag == 2:
            print("\n{} : {}".format(path_d_cmpl + DIR, len(names)))
        if flag == 3:
            print("\n{} : {}".format(path_Processing + DIR, len(names)))
        if flag == 4:
            print("\n{} : {}".format(path_E + DIR, len(names)))
        try:
            id_1 = re.search(regex, names[-1])[2]
            id_2 = re.search(regex, names[-2])[2]
            id_3 = re.search(regex, names[-3])[2]
            id_4 = re.search(regex, names[-4])[2]
            id_5 = re.search(regex, names[-5])[2]
            # user = re.search(regex, names[-1])[1]
            user = DIR
            user_link = "https://www.tiktok.com/@" + user
            names.clear()
            last_urls = ["https://www.tiktok.com/@{}/video/{}".format(user, id_1),
                         "https://www.tiktok.com/@{}/video/{}".format(user, id_2),
                         "https://www.tiktok.com/@{}/video/{}".format(user, id_3),
                         "https://www.tiktok.com/@{}/video/{}".format(user, id_4),
                         "https://www.tiktok.com/@{}/video/{}".format(user, id_5)]

            final_names = []
            try:
                driver.get(user_link)
                error = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div/main/div/p[1]')
                print(error.text)
            except:
                try:
                    e2 = driver.find_element(By.XPATH, '//*[@id="verify-ele"]/div/div[1]/div[2]/div')
                    print(e2)
                except:
                    try:
                        for page in range(1, MAX_PAGE, 1):
                  
                            print("\rLoading page {} ...".format(page), end='', flush=True)
                            for wall in driver.find_elements(By.XPATH,
                                                             '//*[@id="app"]/div[2]/div[2]/div/div[2]/div[2]/div'):
                                for a in wall.find_elements(By.TAG_NAME, 'a'):
                                    if user_link in a.get_attribute('href'):
                                        if a.get_attribute('href') not in final_names:
                                            final_names.append(a.get_attribute('href'))
                                        if a.get_attribute('href') in last_urls:
                                            if len(final_names) == 1:
                                                print(color("\n[*]TikTok videos are already up to date.", fg="cyan"))
                                                raise BreakIt
                                            else:
                                                for ids in (id_1, id_2, id_3, id_4, id_5):
                                                    for final_name in final_names:
                                                        if ids in final_name:
                                                            final_names.remove(final_name)
                                                print(color(
                                                    "\n[+]Target reached, total links {}".format(len(final_names)),
                                                    fg="blue"))
                                            if html_preferred:
                                                if flag == 0:
                                                    path_dir = path + DIR
                                                elif flag == 1:
                                                    path_dir = path_d_process + DIR
                                                elif flag == 2:
                                                    path_dir = path_d_cmpl + DIR
                                                elif flag == 3:
                                                    path_dir = path_Processing + DIR
                                                else:
                                                    path_dir = path_Processing + DIR
                                                write_html(final_names, user, path_dir)
                                                print(color("[+]Successfully appended output links to ", fg="blue"),
                                                      color("links.html", fg="blue", style='bold+italic'))
                                                raise BreakIt
                                            else:
                                                for name in final_names:
                                                    if name == final_names[-1]:
                                                        log(name, user)
                                                    else:
                                                        log(name + "\n", user)
                                                    raise BreakIt

                                                print(color("[+]Successfully written output links to ", fg="blue"),
                                                      color("{}.txt".format(user), fg="blue", style='bold+italic'))
                            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                        print(color("\n[-]Page exceed than MAX_LIMIT", fg="red"))
                        log("Page exceed than MAX_LIMIT.\nTry manually.", "@" + user)
                    except:
                        pass
        except:
            print(color("Video counts less than minimal number, Skipping ....", fg="red", bg="orange"))
            pass


    old_file = open(path + "Users.txt", "r").read().split("\n")
    rearrange_favoured_names = []
    for names in old_file:
        if names not in rearrange_favoured_names:
            rearrange_favoured_names.append(names)
        else:
            print(names)
    rearrange_favoured_names.sort()

    names = []
    for name in rearrange_favoured_names:
        if name in directories:
            names.append(name)
    str_name = ", ".join(names)
    print("{} are already included in update list.".format(names))

    douyin_c = r"D:\#Douyin_Completed"
    douyin_d = r"D:\#Douyin"
    douyin_e = r"E:\#Douyin"

    names = []
    for name in os.listdir(douyin_c):
        if name in directories:
            names.append(name)
    str_name = ", ".join(names)
    print("{} are already included in D/#Douyin_Completed list.".format(names))

    names = []
    for name in os.listdir(douyin_d):
        if name in directories:
            names.append(name)
    str_name = ", ".join(names)
    print("{} are already included in D/#Douyin list.".format(names))

    names = []
    for name in os.listdir(douyin_e):
        if name in directories:
            names.append(name)
    str_name = ", ".join(names)
    print("{} are already included in E/#Douyin list.".format(names))

    for directory in directories:
        if directory is not "":
            user_link_ = "https://www.tiktok.com/@" + directory
            if os.path.exists(path + directory):
                print("Filename {} already exists.".format(directory))
                existing = 5
            elif os.path.exists(path_d_process + directory):
                print("Filename {} already exists.".format(directory))
                existing = 4
            elif os.path.exists(path_d_cmpl + directory):
                print("Filename {} already exists.".format(directory))
                existing = 3
            elif os.path.exists(path_Processing + directory):
                print("Filename {} already exists.".format(directory))
                existing = 2
            elif os.path.exists(path_E + directory):
                print("Filename {} already exists.".format(directory))
                existing = 1
            else:
                existing = 0
            # print(existing)
            if existing == 5:
                if single_directory:
                    tiktok(directory)
                    explore(path + "//outputs//" + directory + ".txt")
                else:
                    if last_name:
                        last_index = os.listdir(path).index(last_name)
                    else:
                        last_index = 0
                    print(color("Last person is {} with index of : {}".format(last_name, last_index), fg="green"))
                    for DIR in os.listdir(path)[last_index:]:
                        tiktok(DIR)
            if existing == 4:
                if single_directory:
                    tiktok(directory)
                    explore(path + "//outputs//" + directory + ".txt")
                else:
                    if last_name:
                        last_index = os.listdir(path_d_process).index(last_name)
                    else:
                        last_index = 0
                    print(color("Last person is {} with index of : {}".format(last_name, last_index), fg="green"))
                    for DIR in os.listdir(path_d_process)[last_index:]:
                        tiktok(DIR)
            if existing == 3:
                if single_directory:
                    tiktok(directory)
                    explore(path + "//outputs//" + directory + ".txt")
                else:
                    if last_name:
                        last_index = os.listdir(path_d_cmpl).index(last_name)
                    else:
                        last_index = 0
                    print(color("Last person is {} with index of : {}".format(last_name, last_index), fg="green"))
                    for DIR in os.listdir(path_d_cmpl)[last_index:]:
                        tiktok(DIR)
            if existing == 2:
                if single_directory:
                    tiktok(directory)
                    explore(path + "//outputs//" + directory + ".txt")
                else:
                    if last_name:
                        last_index = os.listdir(path_Processing).index(last_name)
                    else:
                        last_index = 0
                    print(color("Last person is {} with index of : {}".format(last_name, last_index), fg="green"))
                    for DIR in os.listdir(path_Processing)[last_index:]:
                        tiktok(DIR)
            if existing == 1:
                if single_directory:
                    tiktok(directory)
                    explore(path_E + "//outputs//" + directory + ".txt")
                else:
                    if last_name:
                        last_index = os.listdir(path_E).index(last_name)
                    else:
                        last_index = 0
                    print(color("Last person is {} with index of : {}".format(last_name, last_index), fg="green"))
                    for DIR in os.listdir(path_E)[last_index:]:
                        tiktok(DIR)
            if existing == 0:
                try:
                    print(directory)
                    final_names = []
                    final_counts = []
                    driver.get(user_link_)
                    time.sleep(5)
                    scroll_to_bottom(driver)
                    # print("Scrolled to bottom")
                    if view_count:
                        for wall in driver.find_elements(By.XPATH,
                                                         '//*[@id="app"]/div[2]/div[2]/div/div[2]/div[2]/div'):
                            for count in wall.find_elements(By.XPATH, '//div/div/a/div/div/strong'):
                                final_counts.append(count)
                            for a in wall.find_elements(By.TAG_NAME, 'a'):
                                if user_link_ in a.get_attribute('href'):
                                    if a.get_attribute('href') not in final_names:
                                        final_names.append(a.get_attribute('href'))
                        for name, count in zip(final_names, final_counts):
                            try:
                                count_ = int(count.text)
                            except:
                                count_ = numify.numify(count.text)
                            if name == final_names[-1]:
                                log(name + " : " + str(count_), directory)
                            else:
                                log(name + " : " + str(count_) + "\n", directory)
                    else:
                        for wall in driver.find_elements(By.XPATH,
                                                         '//*[@id="app"]/div[2]/div[2]/div/div[2]/div[2]/div'):
                            for a in wall.find_elements(By.TAG_NAME, 'a'):
                                if user_link_ in a.get_attribute('href'):
                                    if a.get_attribute('href') not in final_names:
                                        final_names.append(a.get_attribute('href'))
                        if html_preferred:
                            write_html(final_names, directory, path + directory)
                            print(color("\n[+]Scrolled to bottom, Total links {}".format(len(final_names)), fg="blue"))
                            print(color("[+]Successfully appended output links to ", fg="blue"),
                                  color("links.html", fg="blue", style='bold+italic'))
                            raise BreakIt
                        else:
                            for name in final_names:
                                if name == final_names[-1]:
                                    log(name, directory)
                                else:
                                    log(name + "\n", directory)

                            print(color("\n[+]Successfully written output links to ", fg="blue"),
                                  color("{}.txt".format(directory), fg="blue", style='bold+italic'))

                            raise BreakIt
                            # explore(path + "//outputs//" + directory + ".txt")
                except:
                    pass

    write_final_script()
    driver.close()
