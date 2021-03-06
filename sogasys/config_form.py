#-*- coding:utf-8 -*-
'''
====================================================================================

   Copyright 2013, 2014 Windy Darian (大地无敌), Studio "Sekai no Kagami" 
   (世界之镜制作组) of Seven Ocean Game Arts （七海游戏文化社
   , 北京航空航天大学学生七海游戏文化社） @ http://sogarts.com

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

====================================================================================
Created on Sep 10, 2013
Configuration form.
@author: Windy Darian (大地无敌)
'''
from panda3d.core import NodePath

from sogal_form import SogalForm
from runtime_data import game_settings
from gui.layout import VLayout
from gui.elements import OptionLabel
from gui.controls import CheckBox, OptionMenu
from gui.direct_controls import SDirectOptionMenu

class ConfigForm(SogalForm):
    '''
    The configuration scene 
    '''
    
    class ConfigCard(NodePath):
        def __init__(self, parent = None, layoutMargin = .05):
            self.parent = parent or aspect2d
            NodePath.__init__(self, 'config_card')
            self.layout = VLayout(parent = self, margin = layoutMargin)
            self.layout.setPos(-1.25, 0, 0.67)
            self.reparentTo(self.parent)
            
            
    def __init__(self):
        '''
        Constructor
        '''
        style = base.getStyle()
        
        SogalForm.__init__(self, fading = True, fading_duration = 0.5, enableMask = True, backgroundColor = style['color']['bg'], sort = 103)
        
        self._style = style
        
        self._cards = {}
        self._graphics = self.ConfigCard(parent = self)
        self._cards['graphics'] = (self._graphics)   #0, graphics
        
        #TODO: 重写ConfigLabel（一个OnscreenText 和一个控件 一行 ） 实现键盘支持

        #resolution = DirectOptionMenu(text="options", scale=0.1,items=["item1","item2","item3"],initialitem=2,
        
        resolution_options = OptionMenu(items = ["Unchanged", "1280x720","1920x1080",'1024x768'],itemcontent = [None,(1280,720),(1920,1080),(1024,768)])
        self._resolution = OptionLabel(self, text = 'Resolution', controlNP = resolution_options)
        self.appendConfigLabel('graphics', self._resolution)   #sresolution
        
        
        fullscreen = CheckBox()
        self._fullscreen = OptionLabel(self, text = 'Full Screen', controlNP = fullscreen)
        self.appendConfigLabel('graphics', self._fullscreen)
        
        self.refreshSettings()
        
    def focused(self):
        self.accept('mouse3', self.hide)
        self.accept('escape', self.hide)
        
    def defocused(self):
        self.ignore('mouse3')
        self.ignore('escape')
        
    def hide(self):
        self._applyResolution()
        SogalForm.hide(self)
        
    def refreshSettings(self):
        self._resolution.controlNP.set(0,0)
        self._fullscreen.controlNP.set(game_settings['full_screen'])
        
    def getStyle(self):
        return self._style
    
    def appendConfigLabel(self, card_key, label):
        '''
        Attach a ConfigLabel to a card.
        @param card_key: defines which card to add this label in.
        @param label: the new label to be added
        Card Keys:
        graphics
        '''
        self._cards[card_key].layout.append(label)
        
    def _applyResolution(self):
        base.setScreenResolution(resolution = self._resolution.controlNP.get(), fullscreen = self._fullscreen.controlNP.get())
        

        