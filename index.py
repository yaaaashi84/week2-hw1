import sys
from PIL import Image
import pyocr
import pyocr.builders
import glob
# import cv2
import datetime

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("ツールなし")
    sys.exit(1)
# 推奨している順で読み込むので、配列の最初に推奨順の1つ目がはいる
tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))
# 例: Will use tool 'Tesseract (sh)'

def image_to_text(file_path):
    txt = tool.image_to_string(
        Image.open(file_path),  # OCRする画像
        lang="eng+jpn",  # 学習済み言語データ
        builder=pyocr.builders.DigitBuilder(Tesseract_layout=6),
    )

    return txt

# res = tool.image_to_string(Image.open(args.image), lang="eng+jpn", builder=pyocr.builders.WordBoxBuilder(tesseract_layout=6))


# out = cv2.imread(args.image)
# for d in res:
#     print d.content
#     print d.position
#     cv2.rectangle(out, d.position[0], d.position[1], (0, 0, 255), 2)


def main():
    file_paths = glob.glob("images/*")  # 置き換え

    txts = [] 
    today = datetime.datetime.now()

    for file_path in file_paths:
        txt = int(image_to_text(file_path))

        txts.append(txt)

    with open("cal.txt", mode="w") as f:
        f.writelines(str(sum(txts)))
            
    with open("cal.txt", "r") as r:
        cal_sum = r.read()

    print(str(today.year) + "/" + str(today.month) + "/" + str(today.day) + "の摂取カロリーは" + str(cal_sum) + "kcalです。")


if __name__ == "__main__":
    main()