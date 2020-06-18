import subprocess as sub
import glob
import imageio
import os

class gifXYZ:
    def __init__(self,
                 xyzFile,
                 gifName,
                 jmolScriptName="jmscriptN.txt",
                 keepFrames=False,
                 fps = 10):
        """
        :param xyzFile: Name of xyz file to read in by jmol
        :type xyzFile:str
        :param gifName: Name of the .gif we will get back out
        :type gifName:str
        :param jmolScriptName: The name of the script template we will be using. Default to jmscriptN
        :type jmolScriptName:str
        :param keepFrames:
        :type keepFrames:bool
        """
        self.xyzFile = xyzFile
        self.gifName = gifName
        self.jmolScriptName = jmolScriptName
        self.keepFrames = keepFrames
        self.fps = fps

    def gifify(self):
        """Generates a a series of images from jmol frames and makes them gifs"""
        sub.call(f"jmol {self.xyzFile} -s {self.jmolScriptName}",shell=True)
        fl = glob.glob("frame*.jpg")
        images = []
        for i in fl:
            images.append(imageio.imread(i))
        if '.gif' in self.gifName:
            self.gifName = self.gifName[:-4]
        imageio.mimsave(f"{self.gifName}.gif", images, fps=self.fps)
        if not self.keepFrames:
            for i in fl:
                os.remove(i)

if __name__=='__main__':
    firstTry = gifXYZ(xyzFile='testScan.xyz',
                      gifName='testScan.gif',
                      jmolScriptName='jmscriptN.txt',
                      keepFrames=True,
                      fps=10)
    firstTry.gifify()