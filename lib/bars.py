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

# Change to match design?
BLACK = (0,0,0)
RED = (90,0,0)
WHITE = (255,255,255)
BLUE = (136,196,255)

class Bars():

    def __init__(self,
        barDestination = surface1,
        barValue = 0,
        needleLength = 148,
        positionX = 150,
        positionY = 150,
        fontSize = twenty,
        backgroundColour = BLACK,
        foregroundColour = BLUE,
        startPosition = 0,
        endPosition = 0,
        maximumValue = 100,
        invert = False,
        doubleLine = 6,
        singleLine = 3,
        displayDivision = 1,
        displayNeedle = True,
        displayPolygon = False,
        dialLabel = False,
        units = False,
        dialType = False):

        self.barDestination = barDestination
        self.barValue = barValue
        self.needleLength = needleLength
        self.positionX = positionX
        self.positionY = positionY
        self.fontSize = fontSize
        self.backgroundColour = backgroundColour
        self.foregroundColour = foregroundColour
        self.startPosition = startPosition
        self.dialType = dialType
        self.maximumValue = maximumValue
        self.invert = invert
        self.doubleLine = doubleLine
        self.singleLine = singleLine
        self.displayDivision = displayDivision
        self.displayNeedle = displayNeedle
        self.displayPolygon = displayPolygon
        self.dialLabel = dialLabel
        self.units = units
        self.endPosition = endPosition
        barWidth = 10

        ##
        ##TEST
        ##
        ## adjust to show same scale for each bar..
        #use scale to adjust angle of bar too!

        # Ratio of actual value
        ratioValue = barValue/(self.maximumValue * 10.0)

        # X value adjustment
        maxY = 400
        adjustedYValue = ratioValue * maxY
        finalYValue = self.positionY - adjustedYValue

        # Y value adjustment
        maxX = 50
        adjustedXValue = ratioValue * maxX
        if self.invert:
            finalXValue = self.positionX - adjustedXValue
        else:
            finalXValue = self.positionX + adjustedXValue

        poly = [
            (self.positionX + barWidth, self.positionY),
            (self.positionX, self.positionY),
            (finalXValue, finalYValue),
            (finalXValue + barWidth, finalYValue)]

        if self.displayPolygon:
            # Render Bar
            pygame.draw.polygon(barDestination, self.foregroundColour, poly)

            # Add label for units
            if self.units:
                unitLabel = str(barValue) + ' ' + self.units
            else:
                unitLabel = str(barValue)

            # Render Value
            self.showValue = self.fontSize.render(unitLabel, 1, self.foregroundColour, self.backgroundColour)
            valueRect = self.showValue.get_rect()
            valueRect.centerx = self.positionX
            valueRect.centery = self.positionY + 30
            self.barDestination.blit(self.showValue, (valueRect))

        if self.dialLabel:
            self.showLabel = self.fontSize.render(self.dialLabel, 1, self.foregroundColour, False)

            if self.invert:
                self.rotatedLabel = pygame.transform.rotate(self.showLabel, -80)
                self.centerx = self.positionX + 100
            else:
                self.rotatedLabel = pygame.transform.rotate(self.showLabel, 80)
                self.centerx = self.positionX - 100

            labelRect = self.rotatedLabel.get_rect()

            # Will need adjusting
            labelRect.centerx = self.centerx
            labelRect.centery = self.positionY - (maxY / 2)
            self.barDestination.blit(self.rotatedLabel, (labelRect))
