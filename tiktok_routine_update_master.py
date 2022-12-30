import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
import subprocess
import re
import glob
from colors import color
from pyhtmlapi import write_html, write_final_script

# from tiktok_var import favoured_names

MAX_PAGE = 15
load_last = False
single_directory = True
view_count = False
html_preferred = True
FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')

regex = "\d+_@(.+)_(\d+)"
path = "D://#Douyin_Routine//"
path_process = "D://#Douyin_Routine_Processing//"
path_E = "E://#Douyin//"

if os.path.exists("C://Users//USER//Desktop//Links.html"):
    x = input("Links.html already exists. Are you sure you want to overwrite?(yes/no) : ")
    if x == "y":
        os.remove("C://Users//USER//Desktop//Links.html")
    if x == "n":
        print("Skipping ......")


def log_users(lines):
    opt_path = path + "Users.txt"
    f = open(opt_path, "a")
    f.write(lines)
    f.close()


old_file = open(path + "Users.txt", "r").read().split("\n")
completed_user = open(path + "Completed_Users.txt", "r").read().split("\n")
rearrange_favoured_names = []
for names in old_file:
    if names not in rearrange_favoured_names:
        rearrange_favoured_names.append(names)
    else:
        print(names)
rearrange_favoured_names.sort()
os.remove(path + "Users.txt")
for rearrange_favoured_name in rearrange_favoured_names:
    if rearrange_favoured_name == rearrange_favoured_names[-1]:
        log_users(rearrange_favoured_name)
    else:
        log_users(rearrange_favoured_name + "\n")

favoured_names = open(path + "Users.txt", "r").read().split("\n")
print("User.txt updated successfully")


class BreakIt(Exception):
    pass


def log_ids(lines, DIR):
    opt_path = path + DIR + "//last_ids.txt"
    f = open(opt_path, "w")
    f.writelines(lines)
    f.close()


def update_last_ids():
    total = len(favoured_names)
    for i, directory in enumerate(favoured_names):
        print("\rUpdating {} / {} ...".format(i + 1, total), end='', flush=True)
        files = glob.glob(path + directory + '/**/*.mp4', recursive=True)
        names = []
        for file in files:
            names.append(os.path.basename(file))
        names.sort()
        try:
            id_1 = re.search(regex, names[-1])[2]
            id_2 = re.search(regex, names[-2])[2]
            id_3 = re.search(regex, names[-3])[2]
            id_4 = re.search(regex, names[-4])[2]
            id_5 = re.search(regex, names[-5])[2]
            final_line = id_1 + "\n" + id_2 + "\n" + id_3 + "\n" + id_4 + "\n" + id_5
            log_ids(final_line, directory)
            # print(final_line)

        except:
            pass


exceptions = ["MS4wLjABAAAAFPjpZpBatGQp_D37orbOd7H2LGytKv1hf2kN7WgytQw6G34rfXB6xMipLrXGga9u", "99hninhtet"]

if __name__ == '__main__':

    # update_last_ids()

    options = webdriver.ChromeOptions()
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "eager"
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options,
                              desired_capabilities=caps)

    favoured_names_test = ["MS4wLjABAAAAFPjpZpBatGQp_D37orbOd7H2LGytKv1hf2kN7WgytQw6G34rfXB6xMipLrXGga9u"]


    def delete(string, status):
        names = []
        for DIR in os.listdir(path):
            for name in os.listdir(path + DIR):
                if status == "start" and name.startswith(string):
                    names.append(path + DIR + "//" + name)
                if status == "end" and name.endswith(string):
                    names.append(path + DIR + "//" + name)
                if status == "in" and string in name:
                    names.append(path + DIR + "//" + name)
                # os.remove(path + DIR + "//" +name)

        print("Total video with {} : {}".format(string, len(names)))


    def explore(_path):
        _path = os.path.normpath(_path)

        if os.path.isdir(_path):
            subprocess.run([FILEBROWSER_PATH, _path])
        elif os.path.isfile(_path):
            subprocess.run([FILEBROWSER_PATH, '/select,', _path])


    def log(lines, user):
        if not os.path.exists(path + "//outputs"):
            os.mkdir(path + "//outputs")
        opt_path = path + "//outputs//" + user + ".txt"
        f = open(opt_path, "a")
        f.writelines(lines)
        f.close()


    def tiktok(DIR, DIR_list, i):
        names = []
        files = []
        flag = 1
        if DIR in completed_user:
            status = 0
            if os.path.exists(path_process + DIR):
                files = glob.glob(path_process + DIR + '/**/*.mp4', recursive=True)
                flag = 0
            elif os.path.exists(path + DIR):
                files = glob.glob(path + DIR + '/**/*.mp4', recursive=True)
                flag = 1
        else:
            status = 1
            if os.path.exists(path + DIR):
                files = glob.glob(path + DIR + '/**/*.mp4', recursive=True)
                flag = 2
            elif os.path.exists(path_E + DIR):
                files = glob.glob(path_E + DIR + '/**/*.mp4', recursive=True)
                flag = 3
        for file in files:
            filename = os.path.basename(file)
            if filename.startswith("_@"):
                pass
            else:
                names.append(filename)
        names.sort()
        if status == 0:
            print(color("\n{}/{} >> {} : {}".format(i + 1, len(DIR_list), DIR, len(names)), fg="green"))
        else:
            print("\n{}/{} >> {} : {}".format(i + 1, len(DIR_list), DIR, len(names)))
        try:
            if DIR in exceptions:
                user = DIR
            else:
                user = re.search(regex, names[-1])[1]
            user_link = "https://www.tiktok.com/@" + user
            # names.clear()
            last_urls = []
            idxx = []
            for i in range(1, 11):
                try:
                    idx = re.search(regex, names[-i])[2]
                    url = "https://www.tiktok.com/@{}/video/{}".format(user, idx)
                    idxx.append(idx)
                    last_urls.append(url)
                except:
                    continue

            final_names = []
            try:
                driver.get(user_link)
                error = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div/main/div/p[1]')
                print(color(error.text, fg="red"))
            except Exception:
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
                                            for ids in idxx:
                                                for final_name in final_names:
                                                    if ids in final_name:
                                                        final_names.remove(final_name)
                                            print(color("\n[+]Target reached, total links {}".format(len(final_names)),
                                                        fg="blue"))

                                            if html_preferred:
                                                if flag == 0:
                                                    path_dir = path_process + DIR
                                                elif flag == 1:
                                                    path_dir = path + DIR
                                                elif flag == 2:
                                                    path_dir = path + DIR
                                                else:
                                                    path_dir = path_E + DIR
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

                                                print(color("[+]Successfully written output links to ", fg="blue"),
                                                      color("{}.txt".format(user), fg="blue", style='bold+italic'))
                                                raise BreakIt
                        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                    print(color("\n[-]Page exceed than MAX_LIMIT", fg="red"))
                    log("Page exceed than MAX_LIMIT.\nTry manually.", "@" + user)
                except:
                    pass
        except:
            print(color("Video counts less than minimal number, Skipping ....", fg="red", bg="orange"))
            pass

    start_from = 0
    # for i, favoured_name in enumerate(favoured_names[start_from:]):
    #     try:
    #         tiktok(favoured_name, favoured_names[start_from:], i)
    #         time.sleep(2)
    #     except FileNotFoundError:
    #         print(favoured_name + " not found")
    #         continue
    f_names = []
    for names in os.listdir(path):
        if not names.startswith("#") or names.endswith(".txt"):
            f_names.append(names)
    for i, favoured_name in enumerate(f_names[start_from:]):
        try:
            tiktok(favoured_name, f_names[start_from:], i)
            time.sleep(2)
        except FileNotFoundError:
            print(favoured_name + " not found")
            continue

    if not html_preferred:
        explore(path + "//outputs")
    write_final_script()
    driver.close()
