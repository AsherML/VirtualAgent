# Using Vero on Zoom


Before the session, there are a few programs and packages that you must install on your computer in order to recreate Vero on your computer

**Installing Python and packages**

1. This project makes use of the python programming language. If you do not have python installed on your computer, you can do so by visiting this link and following the instructions on their webpage: https://www.python.org/downloads/

2. Download the Virtual Agent folder on Cornell Box, which can be found here: https://cornell.app.box.com/folder/138771046416  Install it at a location on your computer you can easily find later

3. Open the VirtualAgent folder and open up the terminal, running the following command: 

        pip install -r requirements.txt
All of the necessary packages should be installed on your computer. 

4. Run the program: there are three different VERO configurations, located in VirtualAgent/scripts/currently_using. Run any of them by clicking on the program icon or running them in any coding environment


**Installing and Configuring OBS**

1. In order to display VERO on Zoom, we need to use OBS. Open OBS and click the plus sign under Scenes. Call it "VERO BASE". 
2. With "VERO BASE" selected, click the plus sign under sources and click Window Capture, selecting the VERO python display. Resize the resulting window so that it fills the whole screen. 
3. Again with "VERO BASE" selected, click the plus sign and then choose Media Source. Name the first one "Crickets" and select the crickets sound effect in resources/sound_effects/crickets.mp3
4. Repeat the above step with resources/sound_effects/working.mp3
5. Create a new scene called "Laughter" using the same method you used to create "VERO BASE"
6. Add resources/sound_effects/laughter.mp3 to the laughter scene in the same way you created the crickets and working effects
7. Click the plus sign under sources with laughter selected and click "image slide show" and select all the gifs titled "laughter" in the resources folder 
7. Go to File-Settings-Hotkeys and create the following shortcuts

- VERO BASE-Switch to Scene: "space button"
- Laughter-Switch to Scene: "l" 
- 'show crickets' and 'hide crickets': 'c'
- 'show working' and 'hide working': w
- 'laugh slide'-'Next Slide': up arrow
- 'laugh slide'- 'Previous Slide': down arrow


**Putting it all Together**

1. Start the python script to display VERO, and start OBS with all the above configurations
2. Click "Start Virtual Camera" in the bottom right corner of OBS
3. Start Zoom **MAKE SURE YOUR VIDEO IS NOT SHOWING WHEN YOU JOIN THE CALL**
4. Click the little arrow next to the video icon in the bottom left and click "Video Settings..."
5. Under Camera select "OBS Virtual Camera"
6. Unclick mirror video if necessary
7. Change your zoom name to VERO




**Animation identifiers**

-There are several motions and sounds to be used as appropriate, whenever your part as the agent warrants a movement. The exact nature of these movements will change depending on the exact configuration used, but here's a somewhat comprehensive list

|       Animation         |How to Activate                                         | Description |
|----------------|-------------------------------|-------------------------------|
|Default| Do nothing |Vero floats and moves around the screen tracking your head movements |
|Speaking|Speak            | Vero glows with a light blue halo|
|Want to Speak| Raise your hand with an open palm facing the camera|Vero will repeatedly grow and shrink|
|Wave | Move your head to the left and then right repeatedly| For greetings and goodbyes; Vero will sway from one side of the screen to the next|
|Agree | Make a "thumbs up" sign with hand | For agreeing with what has been said; Vero will turn green|
|Nod| Nod head up and down, more dramatically than you normally might |Back-channeling response; Vero will nod to indicate that they are engaged and listening |
|Laughter| Press the "L" button and then click the up and down arrows to switch gifs | Used when Vero thinks something's funny, plays a sitcom laugh track and displays cartoon characters
|Working Sound| Click "W"| Used in conjunction with the default animation when VERO needs to look something up or think harder about something
|Crickets| Click "C" | Used in conjunction with the default animation when nothing's happening and when VERO wants to prompt action from the other participants

**Q&A Potential Participant Questions**

_"Vero, help us!"_ or _"Vero, what's going on here?"_
> What would you like to know?**

Need time to find a response
> Let me think about that for a second.
> Let me think about that for a minute please.
> Click "w" to play the working sound if you need to look something up

Dodge a question

> I’m sorry, I’m not sure about that. 
> 
>That is not in my database. 
>
>I am interested in what you think about this. Let’s try to work on this together.
> 
> I don’t think answering this question will be useful for the task at hand. Let’s try to refocus on our goals.

Try to speak but are not acknowledged
>May I say something?

If you misspeak and need to correct
>Sorry team. I think I misunderstood you. What I meant to say was 

To get people talking
> It seems like we are in a brainstorming rut. What are some other categories of ideas we could think about to help our brainstorming?
> 
> We all have a unique perspective to offer! Let’s hear from someone who hasn’t spoken in a while!
> 
> We have come up with a lot of ideas already! Let's come up with as many ideas as possible!
> 
> Let’s say any idea that comes to mind, no matter how weird, strange, or imaginative.
​
#### Potential Paperclip Uses
|       Statement         |Elaboration (if, after you say the idea to the left, your team asks what you mean by that idea)                                         |
|----------------|-------------------------------|
|I have an idea! What about “Battery lead?”| A lead is a metal used in batteries to generate electricity. |
|I have an idea! What about “Button pusher?”|A device that will click or push buttons, such as keys on a keyboard or buttons on a microwave.       | 
|I have an idea! What about “Bubble wand?”| A bubble wand is typically a toy for younger children that consists of a stick with a loop at the end for dipping into a soap solution. Then, when the loop is passed through the air, it creates soap bubbles.|
|I have an idea! What about “Twist tie?” |A twist tie is typically a bendable piece of metal wire covered by either plastic or paper that can be used to tie the openings of bags or containers. | 
|I have an idea! What about “Corn holder?” | A utensil or sharp object that can be inserted into the two ends of corn on a cob in order to eat the corn without having to touch it when it is hot. | 
|I have an idea! What about “Conductor?”| A piece of material that transmits heat, electricity or sound across its surface.  |
| I have an idea! What about “Splint?”| A piece of rigid material that can be used to support a broken bone and keep it in position when it has been set back in place. |
| I have an idea! What about “Drum stick?”| A long, thin piece of solid material that could be used to beat on a drum.|
| I have an idea! What about “To poke?”| To poke is to nudge or press something with an object. You can poke your friend’s arm with your finger to get their attention.|
|I have an idea! What about “Blow dart?” | A sharp projectile that can be shot out of a blowpipe. A blowpipe is a long narrow tube in which an individual blows air through one end and the blow dart shoots out the other end. |
|I have an idea! What about “Needle?” |A needle is a sharp object that can be used when sewing to thread the pieces of fabric together. |
​
​
#### Potential Rubber Band Uses
|       Statement         |Elaboration (if, after you say the idea to the left, your team asks what you mean by that idea)                                         |
|----------------|-------------------------------|
|I have an idea! What about “Bracelet?”|A bracelet is an ornamental band, hoop, or chain worn on the wrist or arm.|
|I have an idea! What about “Wheel tread”?|The tread of a wheel is the rubber on its circumference that makes contact with the road or ground.|
|I have an idea! What about “Slingshot?”|A slingshot is a hand-powered projectile weapon that typically consists of a y-shaped frame with two natural-rubber strips attached to the uprights.|
|I have an idea! What about “Pencil grip”?|A pencil grip is a part fastened to a pencil that is designed to be grasped and held.|
|I have an idea! What about “Heart rate monitor strap”?|A heart rate monitor is a device you wear to measure and display your heart rate. Electrode sensors in a chest strap detect each heartbeat and transmit data.|
|I have an idea! What about “Snare”?	|A snare is a trap for catching birds or small animals. It consists of a loop of wire or rope which pulls tight around an animal.|
|I have an idea! What about “Standard for length”?|A measurement used as the standard for determining all other lengths. |
|I have an idea! What about “Bookmark?”|A bookmark is a material used to mark one’s place in a book.|
|I have an idea! What about “Belt loop?”	|A belt loop is a strip of material in the shape of a loop used to hold a belt in place.|
|I have an idea! What about “Musical instrument?”|A musical instrument is a device used to make music.|

**Things Not to Do**

●  Do not wait until the day-of to practice your setup. Things are a lot less stressful if you know what setup works best for your situation and you may have a team that is very demanding of you.

● Practice speaking/responding to hypothetical questions! Often the hardest part of being a Vero is managing a bunch of different windows and responding in a timely manner.

● Don’t wait too long after a participant asks a question to answer. If you don’t have your bearings enough to answer a question at the same speed you would answer as a person, buy time with something like _Let me think about that._ You can also use the working sound to delay
