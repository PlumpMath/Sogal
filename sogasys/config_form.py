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

from sogal_form import SogalForm
import color_themes

class ConfigForm(SogalForm):
    '''
    The configuration scene 
    '''


    def __init__(self):
        '''
        Constructor
        '''
        SogalForm.__init__(self, fading = True, fading_duration = 0.5, enableMask = True, backgroundColor = color_themes.ilia_bgColor)
        