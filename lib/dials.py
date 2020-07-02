#!/usr/bin/python
# dials.py module

#Copyright (C) 2014 Eilidh Fridlington http://eilidh.fridlington.com

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>

import pygame
import math
from pygame.locals import *
import pygame.gfxdraw
pygame.init()


fifeteen = pygame.font.SysFont("Free Sans", 15)
twenty = pygame.font.SysFont("Free Sans", 20)
sixty = pygame.font.SysFont("Free Sans", 60)

percent = u'\N{PERCENT SIGN}'
millivolt = 'mV'
volt = 'V'
degree = u"\u00B0"

surface1 = pygame.Surface((300,300))

BLACK = (0,0,0)
RED = (90,0,0)
WHITE = (255,255,255)
BLUE = (136,196,255)

class Dials():

    def __init__(self,
        needleDestination = surface1,
        needleValue = 0,
        needleLength = 148,
        positionX = 150,
        positionY = 150,
        fontSize = twenty,
        backgroundColour = BLACK,
        foregroundColour = BLUE,
        startPosition = 0,
        endPosition = 0,
        maximumValue = 100,
        doubleLine = 6,
        singleLine = 3,
        displayDivision = 1,
        displayNeedle = True,
        displayCircle = False,
        dialLabel = False,
        dialType = False):

        self.needleDestination = needleDestination
        self.needleValue = needleValue
        self.needleLength = needleLength
        self.positionX = positionX
        self.positionY = positionY
        self.fontSize = fontSize
        self.backgroundColour = backgroundColour
        self.foregroundColour = foregroundColour
        self.startPosition = startPosition
        self.dialType = dialType
        self.maximumValue = maximumValue
        self.doubleLine = doubleLine
        self.singleLine = singleLine
        self.displayDivision = displayDivision
        self.displayNeedle = displayNeedle
        self.displayCircle = displayCircle
        self.dialLabel = dialLabel
        self.endPosition = endPosition


        length2 = int(self.needleLength / 20)
        length3 = length2 + 5

        degreesDifference = 360 - (self.startPosition +
                        (180 - self.endPosition))

        value = int((self.needleValue * (degreesDifference /
                        (self.maximumValue * 10.0))) + self.startPosition)


        x = self.positionX - math.cos(math.radians(value)) * (self.needleLength - int(self.needleLength / singleLine))
        y = self.positionY - math.sin(math.radians(value)) * (self.needleLength - int(self.needleLength / singleLine))
        x2 = self.positionX - math.cos(math.radians(value - 90)) * length2
        y2 = self.positionY - math.sin(math.radians(value - 90)) * length2
        x3 = self.positionX - math.cos(math.radians(value + 180)) * length3
        y3 = self.positionY - math.sin(math.radians(value + 180)) * length3
        x4 = self.positionX - math.cos(math.radians(value + 90)) * length2
        y4 = self.positionY - math.sin(math.radians(value + 90)) * length2

        xa = self.positionX - math.cos(math.radians(value)) * self.needleLength
        ya = self.positionY - math.sin(math.radians(value)) * self.needleLength

        if self.displayCircle:
            pygame.draw.circle(self.needleDestination, self.backgroundColour, (self.positionX,self.positionY), self.needleLength , 0)

        if self.dialLabel:
            self.showLabel = self.fontSize.render(self.dialLabel, 1, self.foregroundColour, self.backgroundColour)
            labelRect = self.showLabel.get_rect()
            labelRect.centerx = self.positionX
            labelRect.centery = self.positionY - (self.needleLength / 5)
            self.needleDestination.blit(self.showLabel, (labelRect))

        valueDivisions = degreesDifference / 10

        self.indicatorLegend(self.startPosition, 0, self.positionX, self.positionY, self.needleLength,
                        self.needleDestination, self.fontSize,False,True,doubleLine,singleLine,1,self.backgroundColour)

        for divisions in range(1,10):

            if self.needleValue >= (self.maximumValue * divisions):
                self.indicatorLegend((self.startPosition + (valueDivisions * divisions)), (self.maximumValue * divisions),
                                self.positionX, self.positionY, self.needleLength, self.needleDestination, self.fontSize,True,True,self.doubleLine
                                ,self.singleLine,self.displayDivision,self.backgroundColour)

        if self.displayNeedle:
            pygame.draw.aalines(self.needleDestination, self.foregroundColour, True, ((x,y), (x2,y2), (x3, y3), (x4, y4)), False)


        pygame.gfxdraw.arc(self.needleDestination,self.positionX,self.positionY,
                        (self.needleLength - int(self.needleLength / self.singleLine)),(180 + value),self.endPosition,  self.foregroundColour)

        pygame.draw.aaline(self.needleDestination, self.foregroundColour, (x,y),(xa,ya), False)

        pygame.gfxdraw.arc(self.needleDestination,self.positionX,self.positionY,
                        self.needleLength,(180 + self.startPosition), (value - 180), self.foregroundColour)

        pygame.gfxdraw.arc(self.needleDestination,self.positionX,self.positionY,
                        (self.needleLength - int(self.needleLength / self.doubleLine)),(180 + self.startPosition) , (value - 180), self.foregroundColour)

        if self.dialType:
            self.indicatorLegend((180 + self.endPosition), self.needleValue, self.positionX, self.positionY,
                            self.needleLength, self.needleDestination, self.fontSize, False, False,
                            self.doubleLine,self.singleLine,1,self.backgroundColour,self.dialType)
        else:
            self.indicatorLegend((180 + self.endPosition), self.needleValue , self.positionX, self.positionY,
                            self.needleLength, self.needleDestination, self.fontSize, False, False,
                            self.doubleLine,self.singleLine,1,self.backgroundColour)





    def indicatorLegend(self,
                        legendValue,
                        displayValue,
                        positionX,
                        positionY,
                        length,
                        destination,
                        fontSize,
                        doubleLength=False,
                        drawLine=True,
                        doubleLine=6,
                        singleLine=3,
                        displayDivision=1,
                        backgroundColour = WHITE,
                        dialType = False

        ):

        position = (self.positionX,self.positionY)

        if doubleLength:
            lineLength = doubleLine
        else:
            lineLength = singleLine

        x = position[0] - math.cos(math.radians(legendValue)) * length
        y = position[1] - math.sin(math.radians(legendValue)) * length
        xa = position[0] - math.cos(math.radians(legendValue)) * (length - int(length / lineLength))
        ya = position[1] - math.sin(math.radians(legendValue)) * (length - int(length / lineLength))
        xlabel = position[0] - math.cos(math.radians(legendValue)) * (length - int(length / singleLine))
        ylabel = position[1] - math.sin(math.radians(legendValue)) * (length - int(length / singleLine))

        if drawLine:
            pygame.draw.aaline(destination, self.foregroundColour, (x,y),(xa,ya), False)

        if dialType:
            label = fontSize.render(("%s%s" % ((displayValue / displayDivision),self.dialType)),
                                    1, self.foregroundColour, self.backgroundColour)
        else:
            label = fontSize.render((str(displayValue / displayDivision)),
                                    1, self.foregroundColour, self.backgroundColour)

        labelRect = label.get_rect()
        labelRect.centerx = int(xlabel)
        labelRect.centery = int(ylabel)# + 5
        self.needleDestination.blit(label, (labelRect))



