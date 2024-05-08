A simple python script that lets you choose your microphone (I used a virtual audio cable that is tied into my alerts on twitch from obs and my main mic) and then if the audio falls under the threshold (you may need to adjust this to your needs) it alt+f4 your application.

I used this for a phasmophobia challenge.

You'll need to install these packages with pip - I recommend using a package manager like anaconda.
pip install SoundCard
pip install numpy
pip install PyAutoGUI

I am running windows 10. It could have some improvements but for now it's very simple, it runs, let's you select a microphone and then starts so start talking immediately or else it'll alt+f4 your current application!
