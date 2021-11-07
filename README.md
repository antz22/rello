<br />

<p align="middle">
    <img src="https://github.com/antz22/rello/blob/master/imgs/hero.png" width="100%" style="margin:0; padding: 0">
</p>

<br />

<p align="middle">
  Rello is a life-changing motorcycle safety system, implemented through an intelligent machine learning algorithm and insightful and user-friendly web app.
</p>

# Inspiration
We were inspired by the technological advancements being made for self-driving cars; however, after a little brainstorming we realized that motorcyclists’ conditions for safety have not followed the trend of advanced technology protection as car drivers’ have, and current safety measures are not as efficient as they could be. For example, motorcyclists are about 26 times more likely to die than the driver counterparts are in a collision. And the most common type of motorcycle accident involved a car turning left at an intersection. Thus we wanted to make a project that would increase safety for motorcyclists and reduce the number and lethality of accidents.

# What it does
Rello utilizes machine learning to detect dangerous situations in motorcyclists' encounters on the road and uses Twilio to notify loved ones in the case of a serious threat to safety. The machine learning algorithm also keeps data on the user's driving safety reports and habits, allowing users to gain more insights into how defensive they should be driving on the roads, through an easy-to-use and beautiful web interface.

# How we built it
We wanted to be as efficient as possible while creating our program, so we divided our group into two teams: one would work on website development while the other would work on the AI algorithm. The tasks were delegated to each member based on their skill level, allowing each member of the group to learn something newly appropriate for them. After a couple of hours, once both groups had completed , we reconvened and spent the remainder of our time unifying the website and its connections to users with the AI algorithm capable of detecting moving objects like cars.

# Challenges we ran into
One major challenge we ran into was integrating the parts of the program (the website and the algorithm) with each other. Another major challenge we overcame was understanding and implementing a working way to detect moving objects from a moving camera. We initially attempted to use opencv, but we were unable to figure out how to use its code with a video that had a moving camera. We then tried to use yolov3, but ended up struggling for a while as none of us possessed a GPU, but we were eventually able to come up with a solution to use yolov3 with a CPU and were able to get a decent frame rate of 10 to 13 fps.

# Accomplishments that we're proud of
One accomplishment we’re proud of is being able to work with artificial intelligence and develop a model that emulates a feature of a self-driving car in that it can detect other objects like cars and analyze whether or not they are a potential threat. More importantly, what we take more pride in is our ability to effectively work as a team and collaborate in a time crunch.

# What we learned
Some of the things we learned were what yolo was and how it could be used/ is implemented already and how to use chart.js to convey data graphically on our website. Additionally, we also gained insight into what a neural network is, and how it can be used.

# What's next for Rello
In the future, we hope to expand on this project by implementing an alarm system that will be turned on whenever a dangerous threat is detected to further implement safety measures, as a driver might not be able to see a motorcycle, but will be able to hear their alarm, which decreases the chance of an accident.

# Built With

```
bootstrap
css3
firebase
flask
html5
javascript
opencv
python
twilio
yolov3
```

