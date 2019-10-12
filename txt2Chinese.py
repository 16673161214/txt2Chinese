class TxtCleaner:

    def full2half_str(self, uni_str):
        half_chars = []

        for uni_char in uni_str:
            uni_code = ord(uni_char)
            if uni_code == 12288:
                uni_code = 32  # space full to half
            elif 65281 <= uni_code <= 65374:
                uni_code -= 65248
            half_char = chr(uni_code)
            half_chars.append(half_char)
        half_str = ''.join(half_chars)

        return half_str

    def full2half_alphabet_and_num(self, uni_str):
        half_chars = []

        for uni_char in uni_str:
            uni_code = ord(uni_char)
            if uni_code == 12288:
                uni_code = 32
            elif 65296 <= uni_code <= 65305 or 65313 <= uni_code <= 65338 or 65345 <= uni_code <= 65370:
                uni_code -= 65248
            half_char = chr(uni_code)
            half_chars.append(half_char)
        half_str = ''.join(half_chars)

        return half_str

    def half2full_punctuation(self, uni_str, escape_sequence='%*+-./^'):
        full_chars = []

        for uni_char in uni_str:
            uni_code = ord(uni_char)
            if (33 <= uni_code <= 47 or 58 <= uni_code <= 64 or 91 <= uni_code <= 96 or 123 <= uni_code <= 126) \
                    and uni_char not in escape_sequence:
                uni_code += 65248
            full_char = chr(uni_code)
            full_chars.append(full_char)
        full_str = ''.join(full_chars)

        return full_str

    def kangxi2hanzi(self, uni_str):
        hanzi_chars = []
        for uni_char in uni_str:
            uni_code = ord(uni_char)

            if (uni_code >= 12032 and uni_code <= 12255):

                if uni_code == 12032:  # 一
                    uni_code = 19968
                if uni_code == 12036:  # 乙
                    uni_code = 20057
                if uni_code == 12038:  # 二
                    uni_code = 20108
                if uni_code == 12040:  # 人
                    uni_code = 20154
                if uni_code == 12041:  # 儿
                    uni_code = 20799
                if uni_code == 12042:  # 入
                    uni_code = 20837
                if uni_code == 12043:  # 八
                    uni_code = 20843
                if uni_code == 12047:  # 几
                    uni_code = 20960
                if uni_code == 12049:  # 刀
                    uni_code = 20992
                if uni_code == 12050:  # 力
                    uni_code = 21147
                if uni_code == 12052:  # 匕
                    uni_code = 21269
                if uni_code == 12055:  # 十
                    uni_code = 21313
                if uni_code == 12056:  # 卜
                    uni_code = 21340
                if uni_code == 12058:  # 厂
                    uni_code = 21378
                if uni_code == 12060:  # 又
                    uni_code = 21448
                if uni_code == 12061:  # 口
                    uni_code = 21475
                if uni_code == 12063:  # 土
                    uni_code = 22303
                if uni_code == 12064:  # 士
                    uni_code = 22763
                if uni_code == 12067:  # 夕
                    uni_code = 22805
                if uni_code == 12068:  # 大
                    uni_code = 22823
                if uni_code == 12069:  # 女
                    uni_code = 22899
                if uni_code == 12070:  # 子
                    uni_code = 23376
                if uni_code == 12072:  # 寸
                    uni_code = 23544
                if uni_code == 12073:  # 小
                    uni_code = 23567
                if uni_code == 12075:  # 尸
                    uni_code = 23608
                if uni_code == 12077:  # 山
                    uni_code = 23665
                if uni_code == 12079:  # 工
                    uni_code = 24037
                if uni_code == 12080:  # 己
                    uni_code = 24049
                if uni_code == 12081:  # 巾
                    uni_code = 24062
                if uni_code == 12082:  # 干
                    uni_code = 24178
                if uni_code == 12083:  # 幺
                    uni_code = 24186
                if uni_code == 12084:  # 广
                    uni_code = 24191
                if uni_code == 12087:  # 弋
                    uni_code = 24331
                if uni_code == 12088:  # 弓
                    uni_code = 24339
                if uni_code == 12092:  # 心
                    uni_code = 24515
                if uni_code == 12093:  # 戈
                    uni_code = 25096
                if uni_code == 12094:  # 户
                    uni_code = 25143
                if uni_code == 12095:  # 手
                    uni_code = 25163
                if uni_code == 12096:  # 支
                    uni_code = 25903
                if uni_code == 12098:  # 文
                    uni_code = 25991
                if uni_code == 12099:  # 斗
                    uni_code = 26007
                if uni_code == 12100:  # 斤
                    uni_code = 26020
                if uni_code == 12101:  # 方
                    uni_code = 26041
                if uni_code == 12102:  # 无
                    uni_code = 26080
                if uni_code == 12103:  # 日
                    uni_code = 26085
                if uni_code == 12105:  # 月
                    uni_code = 26376
                if uni_code == 12106:  # 木
                    uni_code = 26408
                if uni_code == 12107:  # 欠
                    uni_code = 27424
                if uni_code == 12108:  # 止
                    uni_code = 27490
                if uni_code == 12109:  # 歹
                    uni_code = 27513
                if uni_code == 12111:  # 母
                    uni_code = 27597
                if uni_code == 12112:  # 比
                    uni_code = 27604
                if uni_code == 12113:  # 毛
                    uni_code = 27611
                if uni_code == 12114:  # 氏
                    uni_code = 27663
                if uni_code == 12115:  # 气
                    uni_code = 27668
                if uni_code == 12116:  # 水
                    uni_code = 27700
                if uni_code == 12117:  # 火
                    uni_code = 28779
                if uni_code == 12118:  # 爪
                    uni_code = 29226
                if uni_code == 12119:  # 父
                    uni_code = 29238
                if uni_code == 12122:  # 片
                    uni_code = 29255
                if uni_code == 12123:  # 牙
                    uni_code = 29273
                if uni_code == 12124:  # 牛
                    uni_code = 29275
                if uni_code == 12125:  # 犬
                    uni_code = 29356
                if uni_code == 12126:  # 玄
                    uni_code = 29572
                if uni_code == 12127:  # 玉
                    uni_code = 29577
                if uni_code == 12128:  # 瓜
                    uni_code = 29577
                if uni_code == 12129:  # 瓦
                    uni_code = 29926
                if uni_code == 12130:  # 甘
                    uni_code = 29976
                if uni_code == 12131:  # 生
                    uni_code = 29983
                if uni_code == 12132:  # 用
                    uni_code = 29992
                if uni_code == 12133:  # 田
                    uni_code = 30000
                if uni_code == 12137:  # 白
                    uni_code = 30333
                if uni_code == 12138:  # 皮
                    uni_code = 30382
                if uni_code == 12139:  # 皿
                    uni_code = 30399
                if uni_code == 12140:  # 目
                    uni_code = 30446
                if uni_code == 12141:  # 矛
                    uni_code = 30683
                if uni_code == 12142:  # 矢
                    uni_code = 30690
                if uni_code == 12143:  # 石
                    uni_code = 30707
                if uni_code == 12144:  # 示
                    uni_code = 31034
                if uni_code == 12146:  # 禾
                    uni_code = 31166
                if uni_code == 12147:  # 穴
                    uni_code = 31348
                if uni_code == 12148:  # 立
                    uni_code = 31435
                if uni_code == 12149:  # 竹
                    uni_code = 31481
                if uni_code == 12150:  # 米
                    uni_code = 31859
                if uni_code == 12153:  # 网
                    uni_code = 32593
                if uni_code == 12154:  # 羊
                    uni_code = 32650
                if uni_code == 12155:  # 羽
                    uni_code = 32701
                if uni_code == 12156:  # 老
                    uni_code = 32769
                if uni_code == 12157:  # 而
                    uni_code = 32780
                if uni_code == 12159:  # 耳
                    uni_code = 32819
                if uni_code == 12161:  # 肉
                    uni_code = 32905
                if uni_code == 12162:  # 臣
                    uni_code = 33251
                if uni_code == 12163:  # 自
                    uni_code = 33258
                if uni_code == 12164:  # 至
                    uni_code = 33267
                if uni_code == 12166:  # 舌
                    uni_code = 33292
                if uni_code == 12168:  # 舟
                    uni_code = 33311
                if uni_code == 12170:  # 色
                    uni_code = 33394
                if uni_code == 12173:  # 虫
                    uni_code = 34411
                if uni_code == 12174:  # 血
                    uni_code = 34880
                if uni_code == 12175:  # 行
                    uni_code = 34892
                if uni_code == 12176:  # 衣
                    uni_code = 34915
                if uni_code == 12180:  # 言
                    uni_code = 35328
                if uni_code == 12181:  # 谷
                    uni_code = 35895
                if uni_code == 12182:  # 豆
                    uni_code = 35910
                if uni_code == 12186:  # 赤
                    uni_code = 36196
                if uni_code == 12187:  # 走
                    uni_code = 36208
                if uni_code == 12188:  # 足
                    uni_code = 36275
                if uni_code == 12189:  # 身
                    uni_code = 36523
                if uni_code == 12191:  # 辛
                    uni_code = 36763
                if uni_code == 12192:  # 辰
                    uni_code = 36784
                if uni_code == 12197:  # 里
                    uni_code = 37324
                if uni_code == 12198:  # 金
                    uni_code = 37329
                if uni_code == 12204:  # 雨
                    uni_code = 38632
                if uni_code == 12206:  # 非
                    uni_code = 38750
                if uni_code == 12207:  # 面
                    uni_code = 38754
                if uni_code == 12210:  # 韭
                    uni_code = 38893
                if uni_code == 12211:  # 音
                    uni_code = 38899
                if uni_code == 12215:  # 食
                    uni_code = 39135
                if uni_code == 12216:  # 首
                    uni_code = 39318
                if uni_code == 12217:  # 香
                    uni_code = 39321
                if uni_code == 12219:  # 骨
                    uni_code = 39592
                if uni_code == 12220:  # 高
                    uni_code = 39640
                if uni_code == 12225:  # 鬼
                    uni_code = 39740
                if uni_code == 12229:  # 鹿
                    uni_code = 40575
                if uni_code == 12232:  # 黄
                    uni_code = 40644
                if uni_code == 12233:  # 黍
                    uni_code = 40653
                if uni_code == 12234:  # 黑
                    uni_code = 40657
                if uni_code == 12238:  # 鼓
                    uni_code = 40723
                if uni_code == 12239:  # 鼠
                    uni_code = 40736
                if uni_code == 12240:  # 鼻
                    uni_code = 40763
                if uni_code == 12232:  # 黄
                    uni_code = 40644

            hanzi_char = chr(uni_code)
            hanzi_chars.append(hanzi_char)
        hanzi_str = ''.join(hanzi_chars)
        return hanzi_str

    def buchong2hanzi(self, uni_str):
        hanzi_chars = []
        for uni_char in uni_str:
            uni_code = ord(uni_char)
            if (uni_code >= 11904 and uni_code <= 12031):
                if uni_code == 11918:  # 兀
                    uni_code = 20800
                if uni_code == 11935:  # 母
                    uni_code = 27597
                if uni_code == 11936:  # 民
                    uni_code = 27665
                if uni_code == 11969:  # 虎
                    uni_code = 34382
                if uni_code == 11972:  # 西
                    uni_code = 35199
                if uni_code == 11973:  # 见
                    uni_code = 35265
                if uni_code == 11974:  # 角
                    uni_code = 35282
                if uni_code == 11977:  # 贝
                    uni_code = 36125
                if uni_code == 11979:  # 车
                    uni_code = 26710
                if uni_code == 11987:  # 长
                    uni_code = 38271
                if uni_code == 11988:  # 门
                    uni_code = 38376
                if uni_code == 11992:  # 青
                    uni_code = 38738
                if uni_code == 11993:  # 韦
                    uni_code = 38886
                if uni_code == 11994:  # 页
                    uni_code = 39029
                if uni_code == 11995:  # 风
                    uni_code = 39118
                if uni_code == 11996:  # 飞
                    uni_code = 39134
                if uni_code == 11997:  # 食
                    uni_code = 39135
                if uni_code == 12002:  # 马
                    uni_code = 39532
                if uni_code == 12003:  # 骨
                    uni_code = 39592
                if uni_code == 12004:  # 鬼
                    uni_code = 39740
                if uni_code == 12005:  # 鱼
                    uni_code = 40060
                if uni_code == 12006:  # 鸟
                    uni_code = 40479
                if uni_code == 12007:  # 卤
                    uni_code = 21348
                if uni_code == 12008:  # 麦
                    uni_code = 40614
                if uni_code == 12009:  # 黄
                    uni_code = 40644
                if uni_code == 12012:  # 齐
                    uni_code = 40784
                if uni_code == 12014:  # 齿
                    uni_code = 40831
                if uni_code == 12016:  # 龙
                    uni_code = 40857
                if uni_code == 12019:  # 龟
                    uni_code = 40863
            hanzi_char = chr(uni_code)
            hanzi_chars.append(hanzi_char)
        hanzi_str = ''.join(hanzi_chars)
        return hanzi_str

    def aswhole(self, uni_str):
        uni_str = self.full2half_alphabet_and_num(uni_str)
        uni_str = self.full2half_alphabet_and_num(uni_str)
        uni_str = self.full2half_alphabet_and_num(uni_str)
        uni_str = self.half2full_punctuation(uni_str)
        uni_str = self.kangxi2hanzi(uni_str)
        uni_str = self.buchong2hanzi(uni_str)
        return uni_str


import os
if __name__ == '__main__':
    txtcleaner = TxtCleaner()
    text = txtcleaner.aswhole(text)