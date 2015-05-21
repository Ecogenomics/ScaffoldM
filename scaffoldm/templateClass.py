#!/usr/bin/env python
###############################################################################
#                                                                             #
#    scaffoldm.py                                                         #
#                                                                             #
#    Description!!                                                            #
#                                                                             #
#    Copyright (C) Michael Imelfort                                           #
#                                                                             #
###############################################################################
#                                                                             #
#    This program is free software: you can redistribute it and/or modify     #
#    it under the terms of the GNU General Public License as published by     #
#    the Free Software Foundation, either version 3 of the License, or        #
#    (at your option) any later version.                                      #
#                                                                             #
#    This program is distributed in the hope that it will be useful,          #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of           #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            #
#    GNU General Public License for more details.                             #
#                                                                             #
#    You should have received a copy of the GNU General Public License        #
#    along with this program. If not, see <http://www.gnu.org/licenses/>.     #
#                                                                             #
###############################################################################

__author__ = "Michael Imelfort"
__copyright__ = "Copyright 2014"
__credits__ = ["Michael Imelfort"]
__license__ = "GPLv3"
__maintainer__ = "Michael Imelfort"
__email__ = "mike@mikeimelfort.com"

###############################################################################
###############################################################################
###############################################################################
###############################################################################

# system includes

# local includes

###############################################################################
###############################################################################
###############################################################################
###############################################################################

class TemplateClass():
    """Utilities wrapper"""
    def __init__(self): pass

    def sayHi(self):
        print('write some "REAL" code you bum!')

    def runCommand(self, cmd):
        """Run a command and take care of stdout

        expects 'cmd' to be a string like "foo -b ar"

        returns (stdout, stderr)
        """
        from multiprocessing import Pool
        from subprocess import Popen, PIPE

        p = Popen(cmd.split(' '), stdout=PIPE)
        return p.communicate()

    def parseFile(self, filename):
        """parse a file"""
        import sys
        try:
            with open(filename, "r") as fh:
                for line in fh:
                    print line
        except:
            print "Error opening file:", filename, sys.exc_info()[0]
            raise

    def plot3DFigure(self, points, fileName=""):
        """make a 3d plot"""
        import matplotlib.pyplot as plt
        from mpl_toolkits.mplot3d import axes3d, Axes3D
        from pylab import plot,subplot,axis,stem,show,figure
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(points[:,0],
                   points[:,1],
                   points[:,2],
                   #edgecolors='none',
                   #c=colors,
                   #s=2,
                   #marker='.'
                   )
        # show figure
        if fileName == "":
            plt.show()
        else:
            # or save figure
            plt.savefig(filename)#,dpi=300,format='png')
        plt.close(fig)
        del fig

    def plot2DFigure(self, points, fileName=""):
        """make a 2d plot"""
        import matplotlib.pyplot as plt
        from mpl_toolkits.mplot3d import axes3d, Axes3D
        from pylab import plot,subplot,axis,stem,show,figure
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(points[:,0],
                points[:,1],
                '*g')

        # show figure
        if fileName == "":
            plt.show()
        else:
            # or save figure
            plt.savefig(filename)#,dpi=300,format='png')
        plt.close(fig)
        del fig

