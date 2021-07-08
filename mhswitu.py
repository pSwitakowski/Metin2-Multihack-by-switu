# Generated with Gui Editor by KaMeR1337 ; www.metin2mod.tk

exec ('import sys')
b = sys.modules.keys()
for i in range (len(b)):
    h=b[i]
    r=0
    for g in range(len(h)):
        if h[g] != '.':
            r=r+1
            if r==len(h):
                a=dir(__import__(b[i]))
                for y in range(len(a)):
                    if a[y]=='GetMainCharacterIndex':
                        playerm=b[i]
                    if a[y]=='GetNameByVID':
                        chrm=b[i]
                    if a[y]=='SendShopEndPacket':
                        netm=b[i]
                    if a[y]=='DIK_UP':
                        appm=b[i]
                    if a[y]=='SelectItem':
                        itemm=b[i]
                    if a[y]=='Button':
                        uim=b[i]
                    if a[y]=='mouseController':
                        mouseModulem=b[i]
                    if a[y]=='GetAtlasSize':
                        miniMapm=b[i]
                    if a[y]=='GetMousePosition':
                        wndMgrm=b[i]
imp= 'import '
import dbg
import shop
import math
import ui
import dbg
import wndMgr
import chat
import locale
import time
import background
import os
import chrmgr
import item
import textTail
import shop
import mouseModule
import grp
import uiToolTip
import nonplayer
import systemSetting
import constInfo
from uitooltip import ItemToolTip

exec(imp + chrm + ' as chr')
exec(imp + playerm + ' as player')
exec(imp + netm + ' as net')
exec(imp + appm + ' as app')
exec(imp + itemm + ' as item')
exec(imp + uim + ' as ui')
exec(imp + mouseModulem + ' as mouseModule')
exec(imp + miniMapm + ' as miniMap')
exec(imp + wndMgrm + ' as wndMgr')


boss_list=[107, 112, 108, 192, 193, 191, 194, 394, 591, 534, 533, 691, 2191, 1901, 791, 1304, 2307, 2206, 2091, 993, 492, 1192]
big_font = "Tahoma:20"
medium_font = "Tahoma:16"
small_font = "Tahoma:12"
import time
a=sys.version

if a[2]=='2':
    import petla22 as petla
else:
    import petla27 as petla


class Dialog1(ui.Window):
    def __init__(self):
        ui.Window.__init__(self)
        self.zetka=0
        self.ttt=0
        self.x=0
        self.y=0
        self.z=0
        self.ks=1
        self.speed=5
        self.kordyx=0
        self.kordyy=0
        self.boka=0
        self.bokb=0
        self.skoki=0
        self.targetviddupa=0
        self.targetvid=0
        self.listasindleraaktywacja=0
        self.listavidstart=[]
        self.listavidend=[]
        self.boss_x = 0
        self.boss_y = 0
        self.metin_x = 0
        self.metin_y = 0
        self.BuildWindow()

    def __del__(self):
        ui.Window.__del__(self)

    def BuildWindow(self):
        self.Board = ui.ThinBoard()
        self.Board.SetSize(250, 150)
        self.Board.SetCenterPosition()
        self.Board.AddFlag('movable')
        self.Board.AddFlag('float')
        self.Board.Show()

        self.comp = Component()

        self.zamknij = self.comp.Button(self.Board, '', '', 235, 2, self.zamknij_func, 'd:/ymir work/ui/public/close_button_01.sub', 'd:/ymir work/ui/public/close_button_02.sub', 'd:/ymir work/ui/public/close_button_03.sub')
        self.autor = self.comp.TextLine(self.Board, 'mh by switu', 10, 0, self.comp.RGB(255, 0, 0), small_font)

        self.autorestart = self.comp.ToggleButton(self.Board, 'auto restart', '', 5, 20, (self.autorestart_funcend), (self.autorestart_func), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.wymetkow = self.comp.ToggleButton(self.Board, 'metin detector', '', 5, 50, (self.wymetkow_funend), (self.wymetkow_func), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.bosymetki = self.comp.ToggleButton(self.Board, 'boss detector', '', 5, 80, (self.boss_detectorend), (self.boss_detector_func), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.check_race = self.comp.Button(self.Board, 'check mob race', '', 5, 110, self.check_race_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')

        self.gora = self.comp.Button(self.Board, 'up', '', 150, 20, self.gora_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
        self.dol = self.comp.Button(self.Board, 'down', '', 150, 70, self.dol_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
        self.lewo = self.comp.Button(self.Board, 'left', '', 105, 45, self.lewo_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
        self.prawo = self.comp.Button(self.Board, 'right', '', 195, 45, self.prawo_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')


        self.BoardBoss = ui.ThinBoard()
        self.BoardBoss.SetSize(220, 70)
        self.BoardBoss.SetPosition(100, wndMgr.GetScreenHeight() / 2 - (wndMgr.GetScreenHeight() / 8) + 68)
        self.BoardBoss.AddFlag('float')
        self.BoardBoss.AddFlag('movable')
        self.BoardBoss.Hide()
        self.boss_name = self.comp.TextLine(self.BoardBoss, '', 70, 3, self.comp.RGB(50, 255, 50), big_font)
        self.boss_cords = self.comp.TextLine(self.BoardBoss, '', 85, 25, self.comp.RGB(255, 255, 0), medium_font)
        self.close_boss = self.comp.Button(self.BoardBoss, '', '', 205, 2, lambda: self.BoardBoss.Hide(),'d:/ymir work/ui/public/close_button_01.sub','d:/ymir work/ui/public/close_button_02.sub','d:/ymir work/ui/public/close_button_03.sub')
        self.walk_to_boss_button = self.comp.Button(self.BoardBoss, 'walk up', '', 70, 45, self.walk_to_boss, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')

    def listasindlera(self):
        self.listasindleraaktywacja=1
        self.listasindlera_loop=Loop()
        self.listasindlera_loop.wait(0.04)
        self.listasindlera_loop.on_time_over(self.listasindlera)
        targetvidelo=player.GetMainCharacterIndex()

        if self.targetvid<targetvidelo:
            self.targetvid=targetvidelo
        if self.ttt==200:
            self.ttt=0
            self.listavidend=self.listavidstart
            self.listavidstart=[]
            if self.targetviddupa > self.targetvid:
                self.targetvid=self.targetviddupa

            self.targetviddupa=0


        for i in xrange(self.targetvid-(self.ttt*3000)+50000, self.targetvid-(self.ttt*3000)+53000):
            dystans = player.GetCharacterDistance(i)
            if (dystans > 0 and dystans <19000):
                if (self.ttt==17 or self.ttt==16):
                    self.listavidstart.append(i)
                    if i> self.targetvid and i > self.targetviddupa:
                        self.targetviddupa=i

            if (dystans > 0 and dystans < 19000):
                if not ((self.ttt==17)or(self.ttt==16)):
                    self.listavidstart.append(i)
                    if i > self.targetvid and i > self.targetviddupa:
                        self.targetviddupa=i


        self.ttt=self.ttt+1

    def listasindlerastop(self):
        self.ttt=0
        self.targetviddupa=0
        self.targetvid=0
        self.listavidend=[]
        self.listavidstart=[]
        self.listasindleraaktywacja=0
        self.listasindlera_loop=Loop()
        self.listasindlera_loop.wait(100000000.0)
        self.listasindlera_loop.on_time_over(self.listasindlera)

    def zamknij_func(self):
        self.Board.Hide()
        if(self.BoardBoss.IsShow()):
            self.BoardBoss.Hide()

    def gora_func(self):
        myVid = player.GetMainCharacterIndex()
        chr.SelectInstance(myVid)
        (x, y, z) = player.GetMainCharacterPosition()
        chr.SetPixelPosition(int(x), int(y) - 2000, int(z))
        player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
        player.SetSingleDIKKeyState(app.DIK_UP, FALSE)

    def dol_func(self):
        myVid = player.GetMainCharacterIndex()
        chr.SelectInstance(myVid)
        (x, y, z) = player.GetMainCharacterPosition()
        chr.SetPixelPosition(int(x), int(y) + 2000, int(z))
        player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
        player.SetSingleDIKKeyState(app.DIK_UP, FALSE)

    def lewo_func(self):
        myVid = player.GetMainCharacterIndex()
        chr.SelectInstance(myVid)
        (x, y, z) = player.GetMainCharacterPosition()
        chr.SetPixelPosition(int(x) - 2000, int(y), int(z))
        player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
        player.SetSingleDIKKeyState(app.DIK_UP, FALSE)

    def prawo_func(self):
        myVid = player.GetMainCharacterIndex()
        chr.SelectInstance(myVid)
        (x, y, z) = player.GetMainCharacterPosition()
        chr.SetPixelPosition(int(x) + 2000, int(y), int(z))
        player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
        player.SetSingleDIKKeyState(app.DIK_UP, FALSE)

    def check_race_func(self):
        i = player.GetTargetVID()
        chr.SelectInstance(i)
        race = chr.GetRace(i)
        self.race_text = self.comp.TextLine(self.Board, '' + str(int(race)), 98, 113, self.comp.RGB(250, 255, 650), small_font)


    def autorestart_func(self):
        self.autorestart_func_loop=Loop()
        self.autorestart_func_loop.wait(3.0)
        self.autorestart_func_loop.on_time_over(self.autorestart_func)
        maxhp=player.GetStatus(player.MAX_HP)
        aktualnehp=player.GetStatus(player.HP)
        if float(aktualnehp) / float(maxhp) * 100 < int(0):
            player.SetAttackKeyState(FALSE)
            net.SendChatPacket('/restart_here')

    def autorestart_funcend(self):
        self.autorestart_func_loop=Loop()
        self.autorestart_func_loop.wait(100000000.0)
        self.autorestart_func_loop.on_time_over(self.autorestart_func)


    def wymetkow_func(self):
        self.wymetkow_func_loop=Loop()
        self.wymetkow_func_loop.wait(5.0)
        self.wymetkow_func_loop.on_time_over(self.wymetkow_func)
        player.RequestUseLocalQuickSlot(0)
        player.RequestUseLocalQuickSlot(0)
        player.RequestUseLocalQuickSlot(1)
        player.RequestUseLocalQuickSlot(1)
        player.RequestUseLocalQuickSlot(2)
        player.RequestUseLocalQuickSlot(2)
        player.RequestUseLocalQuickSlot(3)
        player.RequestUseLocalQuickSlot(3)
    def wymetkow_funend(self):
        self.wymetkow_func_loop=Loop()
        self.wymetkow_func_loop.wait(100000000.0)
        self.wymetkow_func_loop.on_time_over(self.wymetkow_func)


    def boss_detector_func(self):
        global boss_list
        self.boss_detector_loop = Loop()
        self.boss_detector_loop.wait(0.004)
        self.boss_detector_loop.on_time_over(self.boss_detector_func)
        o = player.GetMainCharacterIndex()
        if self.ks == 500:
            self.ks = 0
        for i in xrange(o - (self.ks * 2000) + 50000, o - (self.ks * 2000) + 52000):
            Odleglosc = player.GetCharacterDistance(i)
            if Odleglosc > 0:
                Typ = chr.GetInstanceType(i)
                if Typ == 0:
                    chr.SelectInstance(i)
                    Race = chr.GetRace(i)
                    for k in boss_list:
                        if Race == int(k):
                            imie = chr.GetNameByVID(i)
                            chr.SelectInstance(i)
                            (X, Y, Z) = chr.GetPixelPosition(i)
                            self.boss_x = int(X)
                            self.boss_y = int(Y)
                            X = X / 100
                            Y = Y / 100
                            X = str(int(X))
                            Y = str(int(Y))
                            self.boss_name.SetText('{}'.format(imie))
                            self.boss_cords.SetText('({},{})'.format(X, Y))
                            self.BoardBoss.Show()

        self.ks += 1

    def boss_detectorend(self):
        self.boss_detector_loop=Loop()
        self.boss_detector_loop.wait(100000000.0)
        self.boss_detector_loop.on_time_over(self.boss_detectorend)
        self.ks = 1
        self.boss_name.SetText('')
        self.boss_cords.SetText('')
        if(self.BoardBoss.IsShow()):
            self.BoardBoss.Hide()

    def walk_to_boss(self):
        myVid = player.GetMainCharacterIndex()
        (myx, myy, myz) = player.GetMainCharacterPosition()
        distance = 135
        if myx < self.boss_x:
            self.aimx = int(self.boss_x) - distance
        else:
            self.aimx = int(self.boss_x) + distance
        if myy < self.boss_y:
            self.aimy = int(self.boss_y) - distance
        else:
            self.aimy = int(self.boss_y) + distance
        chr.MoveToDestPosition(int(myVid), self.boss_x, self.boss_y)


    def OpenWindow(self):
        if self.Board.IsShow():
            self.Board.Hide()
        else:
            self.Board.Show()
    def Close(self):
        self.Board.Hide()

class Component:
	def Button(self, parent, buttonName, tooltipText, x, y, func, UpVisual, OverVisual, DownVisual):
		button = ui.Button()
		if parent != None:
			button.SetParent(parent)
		button.SetPosition(x, y)
		button.SetUpVisual(UpVisual)
		button.SetOverVisual(OverVisual)
		button.SetDownVisual(DownVisual)
		button.SetText(buttonName)
		button.SetToolTipText(tooltipText)
		button.Show()
		button.SetEvent(func)
		return button

	def ToggleButton(self, parent, buttonName, tooltipText, x, y, funcUp, funcDown, UpVisual, OverVisual, DownVisual):
		button = ui.ToggleButton()
		if parent != None:
			button.SetParent(parent)
		button.SetPosition(x, y)
		button.SetUpVisual(UpVisual)
		button.SetOverVisual(OverVisual)
		button.SetDownVisual(DownVisual)
		button.SetText(buttonName)
		button.SetToolTipText(tooltipText)
		button.Show()
		button.SetToggleUpEvent(funcUp)
		button.SetToggleDownEvent(funcDown)
		return button

	def EditLine(self, parent, editlineText, x, y, width, heigh, max):
		SlotBar = ui.SlotBar()
		if parent != None:
			SlotBar.SetParent(parent)
		SlotBar.SetSize(width, heigh)
		SlotBar.SetPosition(x, y)
		SlotBar.Show()
		Value = ui.EditLine()
		Value.SetParent(SlotBar)
		Value.SetSize(width, heigh)
		Value.SetPosition(1, 1)
		Value.SetMax(max)
		Value.SetLimitWidth(width)
		Value.SetMultiLine()
		Value.SetText(editlineText)
		Value.Show()
		return SlotBar, Value

	def TextLine(self, parent, textlineText, x, y, color, font):
		textline = ui.TextLine()
		textline.SetFontName(font)
		if parent != None:
			textline.SetParent(parent)
		textline.SetPosition(x, y)
		if color != None:
			textline.SetFontColor(color[0], color[1], color[2])
		textline.SetText(textlineText)
		textline.Show()
		return textline

	def RGB(self, r, g, b):
		return (r*255, g*255, b*255)

	def SliderBar(self, parent, sliderPos, func, x, y):
		Slider = ui.SliderBar()
		if parent != None:
			Slider.SetParent(parent)
		Slider.SetPosition(x, y)
		Slider.SetSliderPos(sliderPos / 100)
		Slider.Show()
		Slider.SetEvent(func)
		return Slider

	def ExpandedImage(self, parent, x, y, img):
		image = ui.ExpandedImageBox()
		if parent != None:
			image.SetParent(parent)
		image.SetPosition(x, y)
		image.LoadImage(img)
		image.Show()
		return image

	def ComboBox(self, parent, text, x, y, width):
		combo = ui.ComboBox()
		if parent != None:
			combo.SetParent(parent)
		combo.SetPosition(x, y)
		combo.SetSize(width, 15)
		combo.SetCurrentItem(text)
		combo.Show()
		return combo

	def ThinBoard(self, parent, moveable, x, y, width, heigh, center):
		thin = ui.ThinBoard()
		if parent != None:
			thin.SetParent(parent)
		if moveable == TRUE:
			thin.AddFlag('movable')
			thin.AddFlag('float')
		thin.SetSize(width, heigh)
		thin.SetPosition(x, y)
		if center == TRUE:
			thin.SetCenterPosition()
		thin.Show()
		return thin

	def Gauge(self, parent, width, color, x, y):
		gauge = ui.Gauge()
		if parent != None:
			gauge.SetParent(parent)
		gauge.SetPosition(x, y)
		gauge.MakeGauge(width, color)
		gauge.Show()
		return gauge

	def ListBoxEx(self, parent, x, y, width, heigh):
		bar = ui.Bar()
		if parent != None:
			bar.SetParent(parent)
		bar.SetPosition(x, y)
		bar.SetSize(width, heigh)
		bar.SetColor(0x77000000)
		bar.Show()
		ListBox=ui.ListBoxEx()
		ListBox.SetParent(bar)
		ListBox.SetPosition(0, 0)
		ListBox.SetSize(width, heigh)
		ListBox.Show()
		scroll = ui.ScrollBar()
		scroll.SetParent(ListBox)
		scroll.SetPosition(width-15, 0)
		scroll.SetScrollBarSize(heigh)
		scroll.Show()
		ListBox.SetScrollBar(scroll)
		return bar, ListBox

class Loop(ui.ScriptWindow):
    def __init__(self):
        ui.ScriptWindow.__init__(self)
        self.eventTimeOver = lambda *arg: None
        self.eventExit = lambda *arg: None

    def __del__(self):
        ui.ScriptWindow.__del__(self)

    def wait(self, waitTime):
        curTime = time.clock()
        self.endTime = curTime + waitTime
        self.Show()

    def Close(self):
        self.Hide()

    def Destroy(self):
        self.Hide()

    def on_time_over(self, event):
        self.eventTimeOver = ui.__mem_func__(event)

    def SAFE_SetExitEvent(self, event):
        self.eventExit = ui.__mem_func__(event)

    def OnUpdate(self):
        lastTime = max(0, self.endTime - time.clock())
        if 0 == lastTime:
            self.Close()
            self.eventTimeOver()

        else:
            return

dialog = Dialog1()
dialog.Show()
dialog_loop=Loop()
dialog_loop.wait(99999999.0)
