from pathlib import Path
import json
import html

SITE = Path(__file__).resolve().parent
DATA = SITE.parent / "data"

articles = [
    {
        "id": "a9",
        "slug": "orange-bowl-vt-defeats-penn-state-cfp",
        "type": "CFP Quarterfinal",
        "title": "Hokies Dismantle Penn State in Miami, Advance to CFP Semifinal",
        "dek": "Virginia Tech 45, Penn State 28. Woodside broke the national TD record. Vick Jr. broke the ACC passing yards record. The quarterfinal wasn't close.",
        "author": "Commonwealth Wire Staff",
        "location": "Miami, FL — Capital One Orange Bowl",
        "year": 2028,
        "week": "CFP Quarterfinal",
        "featuredTeam": "Virginia Tech",
        "featuredPlayer": "Marquis Woodside",
        "tags": ["Virginia Tech", "Penn State", "CFP", "Orange Bowl", "Marquis Woodside"],
        "relatedArticleIds": ["a8", "a7", "a1"],
        "heroImage": "assets/game/orange-bowl-winner.jpg",
        "heroTheme": "vt",
        "published": "2028 CFP Quarterfinal",
        "gamePhotos": [
            {
                "src": "assets/game/orange-bowl-woodside-potg.jpg",
                "caption": "Marquis Woodside: Player of the Game. 9 catches, 157 yards, 3 touchdowns.",
                "label": "POTG",
            },
            {
                "src": "assets/game/orange-bowl-box-score.jpg",
                "caption": "Virginia Tech 45, Penn State 28. The Hokies dominated in every phase.",
                "label": "Box Score",
            },
            {
                "src": "assets/game/woodside-national-record.jpg",
                "caption": "Woodside broke the national single-season receiving touchdowns record with 29.",
                "label": "Record Broken",
            },
            {
                "src": "assets/game/vick-acc-record.jpg",
                "caption": "Mike Vick Jr. set the ACC single-season passing yards record in the same game.",
                "label": "Record Broken",
            },
            {
                "src": "assets/game/orange-bowl-scoring-q1q2.jpg",
                "caption": "Scoring summary through the first half — a tight game that VT broke open.",
                "label": "Scoring",
            },
            {
                "src": "assets/game/orange-bowl-scoring-q4.jpg",
                "caption": "The fourth quarter was all Virginia Tech: 21 unanswered before Penn State added a garbage score.",
                "label": "Q4 Explosion",
            },
        ],
        "keyStats": [
            ("Final", "Virginia Tech 45, Penn State 28"),
            ("Records", "VT 13-1 | PSU 11-2"),
            ("Woodside", "9 REC, 157 YDS, 3 TD — POTG"),
            ("Vick Jr.", "24-34, 281 YDS, 4 TD, 2 INT, 167.0 RTG"),
            ("Overton", "11 CAR, 131 YDS, 11.9 AVG, 1 TD"),
            ("3rd Down", "VT 7-of-12 (58%) | PSU 2-of-8 (25%)"),
            ("Total Offense", "VT 469 YDS | PSU 416 YDS"),
            ("Record Broken", "Woodside: 29 season TDs — all-time national record"),
        ],
        "body": [
            "MIAMI — They called it a quarterfinal, but Virginia Tech turned the Capital One Orange Bowl into a coronation. Final score: Virginia Tech 45, Penn State 28. And it wasn't that close.",
            "The Hokies dismantled the Lions one explosive play at a time, built a 21-7 halftime lead, survived a brief Penn State surge in the third, then detonated for 21 points in the fourth quarter that turned a game into a statement. Virginia Tech is heading to the CFP semifinal. And Marquis Woodside is headed somewhere no freshman has ever been.",
            "Woodside's three-touchdown night pushed his season receiving touchdown total to 29 — breaking the national single-season record that had stood since Bailey Zappe's 62-pass, 62-catch fever dream season in 2021. The comparison is absurd, the record is real, and the kid who did it is 19 years old from Hampton, Virginia, playing for a school that bet on him when nobody else would.",
            "Mike Vick Jr. was the other record-breaker. His 281 passing yards tonight pushed his 2028 season total past the ACC single-season passing yards record — another line in the books belonging to a Hokie. On a night with two national records shattered before the confetti cleared, Blacksburg will not be short on material this offseason.",
            "The game itself started as a track meet. Penn State quarterback Miles Lewis opened with a 41-yard strike to Clayton Byard on the Lions' first meaningful possession, and suddenly it felt like the Big Ten speed could match Virginia Tech's firepower. It lasted one series. Vick Jr. answered immediately — a 32-yard bullet to Woodside in the back of the end zone, perfectly placed, instantly followed by the crowd realizing that this Lions secondary was not equipped to cover what Virginia Tech was about to deploy.",
            "The second quarter is where the night was decided. Safety Doug Bulluck returned an interception 51 yards for a touchdown — the play that took Penn State's momentum and redirected it toward the exits. Penn State tried to answer, and Lewis did connect with Tory Firth for a stunning 83-yard score that briefly re-tightened the margin. But Virginia Tech's offensive machine doesn't panic; it just loads again. Donte Hawthorne caught a 6-yard Vick Jr. pass before halftime, and the Hokies went into the locker room ahead 21-17, completely in control of their own fate.",
            "The third quarter was a field goal exchange — both defenses briefly found their footing, Penn State's Javier Amano hit from 37, Trinity Rodman hit from 26 for the Hokies, and the score sat 24-20 with 15 minutes standing between Virginia Tech and a semifinal berth. This is where Penn State must have believed.",
            "Then Woodside happened. A 53-yard reception on the first possession of the fourth quarter, Vick Jr. finding him in stride over the middle with the kind of throw that requires both arm and trust. It pushed the lead to 31-20. Penn State countered with a Lewis touchdown run and a two-point conversion — 31-28 — and for approximately two minutes, there was a game.",
            "Jeff Overton ended the discussion. The junior running back took a handoff, found a crease on the left side, and did not stop running for 63 yards. By the time Penn State's defense reacted, Overton was already in the end zone and the Hokies were up 38-28 with the clock bleeding. Woodside added a 3-yard touchdown grab — his record-breaker, his 29th of the season — with 1:43 remaining, and Miami handed Virginia Tech the official placard: Quarterfinal Playoff Game Winner.",
            "Vick Jr. finished 24-of-34 for 281 yards, four touchdowns, and two interceptions, posting a 167.0 passer rating. His legs added scramble damage throughout. Overton ran 11 times for 131 yards and a score, a 11.9 yards-per-carry average that tells you Penn State had no answer for what happened when the Hokies went off-schedule. Brownlee added 7 catches for 65 yards, continuing his quiet Heisman case in a game where Woodside was the headline.",
            "The team stat line was dominant. Virginia Tech gained 469 total yards. Penn State gained 416, impressive against any other opponent, insufficient against a Hokies team that went 7-of-12 on third down and kept the chains moving whenever the Lions appeared ready to make a stop. Penn State converted 2-of-8 on third down. That number explains the final score as efficiently as any highlight.",
            "Virginia Tech is now 13-1. Marquis Woodside has 29 receiving touchdowns. Mike Vick Jr. holds the ACC single-season passing yards record. The Hokies are four quarters from the national championship game. Somewhere in Charlottesville, this season still does not make sense. In Blacksburg, it is the only thing that does.",
        ],
    },
    {
        "id": "a8",
        "slug": "woodside-the-kid-charlottesville-left-behind",
        "type": "Feature",
        "title": "The Kid Charlottesville Left Behind",
        "dek": "Marquis Woodside grew up in UVA's backyard. They didn't want him. Virginia Tech did. Now he owns every award in college football.",
        "author": "Marcus Vick",
        "location": "Blacksburg, VA",
        "year": 2028,
        "week": "CFP",
        "featuredTeam": "Virginia Tech",
        "featuredPlayer": "Marquis Woodside",
        "tags": ["Marquis Woodside", "Virginia Tech", "Heisman", "Feature", "Virginia"],
        "relatedArticleIds": ["a9", "a7", "a1"],
        "heroImage": "assets/game/woodside-national-record.jpg",
        "heroTheme": "vt",
        "published": "2028 CFP",
        "gamePhotos": [
            {
                "src": "assets/game/woodside-national-record.jpg",
                "caption": "Woodside set the national single-season receiving touchdowns record — 29 in his freshman year.",
                "label": "Record Broken",
            },
            {
                "src": "assets/game/national-records-book.jpg",
                "caption": "His name sits above Barry Sanders in the national record book. As a freshman.",
                "label": "Record Book",
            },
        ],
        "keyStats": [
            ("2028 Stats", "96 REC, 1,698 YDS, 26 TD (regular season)"),
            ("Awards", "Heisman, Biletnikoff, Maxwell, Walter Camp, Shaun Alexander"),
            ("Record", "National Single-Season Receiving TDs (29 after Orange Bowl)"),
            ("Hometown", "Charlottesville, VA"),
            ("Passed on by", "Virginia"),
            ("Signed with", "Virginia Tech"),
            ("Year", "Freshman"),
        ],
        "body": [
            "The office at Virginia's football facility is quiet on the days they don't make offers. Nobody announces the names they pass on. There is no ceremony for a rejection, no press conference for the kid who didn't make the board. Charlottesville just stays quiet and the bus route that runs past Scott Stadium keeps running, and the kid who grew up on that route has to find somewhere else to go.",
            "That kid was Marquis Woodside.",
            "He grew up three miles from UVA's campus, a skinny receiver with slippery feet and a reputation for making catches in practice that never seemed to translate into serious recruiting attention. He played at Monticello High School and he played well — most of the people in his program will tell you he played better than anyone gave him credit for — but the Cavaliers never called. Not seriously. There were soft contacts, the kind of semi-interest that programs show to local kids they want to string along without committing to, but when Virginia's 2028 class closed, Marquis Woodside was not in it.",
            "He was ranked. He was watched. He was not offered.",
            "The message was not subtle. You are good, but you are not good enough for us. You are local, but not local enough for a scholarship. You can grow up in our shadow and we still would rather look elsewhere. It is the kind of institutional shrug that happens hundreds of times per recruiting cycle, forgotten the moment it's delivered. Virginia Tech did not forget. Virginia Tech made the call.",
            "Wide receivers coach Derrick Chambers was the first to sit with Woodside's family in the living room of their off-Barracks Road apartment. He came in with tape. He came in with a plan. He came in with the central pitch that Virginia Tech had been refining for two years: Vick Jr. is going to be throwing deep routes to someone every Saturday, and that someone should be you. The family listened. Woodside listened harder than anyone in the room. By the end of January, he had signed. By August camp, he had already made three defensive backs look like they were standing still.",
            "The 2028 regular season unfolded the way Virginia Tech's offensive staff had drawn it up, except faster. Woodside caught 96 passes. He piled up 1,698 receiving yards. He crossed the end zone 26 times, including four-touchdown performances against Wake Forest and Miami in the ACC Championship. By November, opposing defensive coordinators had stopped game-planning for him as a variable and started game-planning around him as a certainty. Every coverage rotation began with a question: where is Woodside, and is anyone brave enough to be alone with him?",
            "The answer was almost always no. Virginia Tech's offense was already designed to stress every level of a defense — Vick Jr. throws from a clean platform, Overton keeps the box honest, and Brownlee stretches the field enough that someone has to account for him. But Woodside changed the arithmetic. A defense that commits safety help over the top leaves the flat open. A defense that plays man leaves a freshman on an island he was born to own. The Hokies exploited both choices with equal enthusiasm, and by the ACC Championship the game plan had become transparent and unstoppable simultaneously.",
            "The Heisman ceremony in New York was the kind of night that gets replicated in motivational posts for decades. Woodside sat in the front row of the Marriott Marquis ballroom wearing a suit he'd bought himself, flanked by his mother Renee and his high school position coach Leon Barrett, who had spent four years telling anyone in Charlottesville who would listen that this kid was going to embarrass somebody. On stage, with the trophy in his hands, Woodside did not cry. He looked at the camera with the same flat-calm expression he uses when the defensive back across from him is talking. Then he said three sentences: 'I'm from Charlottesville. I played in Charlottesville for four years. They know what they passed on.' He sat down. The room did not stop applauding for a long time.",
            "He also took the Biletnikoff Award. The Maxwell Award. The Walter Camp Award. The Shaun Alexander Freshman of the Year Award — a distinction that recognizes the best freshman in college football and has never before been won by someone who simultaneously won the Heisman. The five-trophy sweep did not just make history. It erased every quiet room in Charlottesville where the decision was made not to call.",
            "Virginia's season ended at 9-3, the rivalry loss to Virginia Tech burning the most. The Cavaliers watched from home as Woodside caught touchdowns in Charlotte and Miami. The Cavaliers' recruiting staff, to their credit, has already circled the Hampton-Charlottesville corridor with renewed attention for the 2029 class. Nobody in Blacksburg thinks that is a coincidence.",
            "There is a version of this story where Woodside signs with Virginia and catches touchdowns in blue and orange and the whole thing becomes a nice local story. A player who stayed home. That is not this story. This story is about what happens when a program underestimates its own neighborhood, and what happens when another program does not. Virginia Tech believed in Woodside before the tape made it obvious. The tape eventually made it obvious to everyone, and now the trophy case belongs to Blacksburg.",
            "Marquis Woodside is nineteen years old. He has never played a college game outside the state of Virginia or Florida. He has the Heisman Trophy and every major individual award in college football and a national receiving touchdowns record that is going to outlast most of the careers of the players in his recruiting class. He is a freshman.",
            "The bus still runs past Scott Stadium. Nobody on it is thinking about the offer that never came. Woodside is not on the bus anymore. He is in Miami preparing for a CFP semifinal, and the only direction he is looking is forward.",
        ],
    },
    {
        "id": "a7",
        "slug": "acc-championship-woodside-heisman-miami",
        "type": "ACC Championship",
        "title": "Virginia Tech Outlasts Miami in 58-55 ACC Championship Classic",
        "dek": "The Hokies survived Miami's haymakers, won an overtime track meet, and left Charlotte with Woodside at the front of the Heisman race and Brownlee right behind him.",
        "author": "Commonwealth Wire Staff",
        "location": "Charlotte, NC",
        "year": 2028,
        "week": "ACC Championship",
        "featuredTeam": "Virginia Tech",
        "featuredPlayer": "Marquis Woodside",
        "tags": ["Virginia Tech", "Miami", "ACC Championship", "Heisman", "Marquis Woodside"],
        "relatedArticleIds": ["a8", "a1", "a2"],
        "heroImage": "assets/action/acc-championship-hero.svg",
        "heroTheme": "vt",
        "published": "2028 ACC Championship",
        "keyStats": [
            ("Final", "Virginia Tech 58, Miami 55 (OT)"),
            ("Records", "Virginia Tech 12-1, Miami 10-3"),
            ("Woodside", "9 REC, 196 YDS, 4 TD"),
            ("Vick Jr.", "22-29, 361 YDS, 5 TD"),
            ("Brownlee", "61-yard TD, Heisman top five"),
            ("Overton", "21 CAR, 190 YDS, 3 TD"),
        ],
        "body": [
            "The ACC Championship did not settle down. It never even pretended to. Virginia Tech and Miami turned Charlotte into a five-quarter sprint, traded explosives like neither defense had been invited, and left the Hokies standing at midfield with a 58-55 overtime win, a conference trophy, and the kind of Heisman case that voters can feel before they even open the stat sheet.",
            "Miami made the first half feel dangerous. The Hurricanes scored 10 in the first quarter, then detonated for 21 in the second, including an 81-yard strike to DeMarco Hodges and a one-yard Dennard Fontaine plunge that briefly made the night feel like it was tilting green and orange. Virginia Tech did not flinch. Mike Vick Jr. answered with distance throws, tempo, and the calm of a quarterback who knows he has the most frightening receiver in the country working downfield.",
            "That receiver was Marquis Woodside, and the championship game became his closing argument. Woodside caught nine passes for 196 yards and four touchdowns, stacking scores of 64, 41, 2, and 25 yards across regulation and overtime. Earlier in the postseason push, he had already broken the ACC single-season receiving yards record. Against Miami, he added the signature game: not a stat pad, not a blowout souvenir, but four touchdowns in a title fight that demanded every one of them.",
            "The scoring trend told the story. Miami kept landing big shots; Virginia Tech kept answering with longer drives and cleaner situational football. The Hurricanes finished with 553 yards and 451 through the air, but the Hokies countered with 612 total yards, 251 on the ground, and an absurd 8-for-11 mark on third down. When the game became a possession-by-possession pressure test, Virginia Tech had the sturdier engine.",
            "Vick Jr. was the accelerator. He went 22-of-29 for 361 yards, five touchdowns and one interception, spreading the field just enough to keep Miami from living over Woodside. Nick Brownlee's 61-yard touchdown in the first quarter mattered beyond the scoreboard because it reminded everyone that the Hokies' Heisman race is not a one-man billboard. Brownlee is there too, sitting in the national Heisman picture and forcing defenses to pay for every extra body they lean toward Woodside.",
            "The balance came from Jeff Overton, who turned 21 carries into 190 yards and three touchdowns. His 48-yard third-quarter run changed the texture of the game. His four-yard overtime score gave Virginia Tech the lead back when the whole night was wobbling. And after Miami answered with a 63-yard two-point conversion pass in the fourth quarter and a field goal in overtime, the Hokies still had one more answer.",
            "That final answer was vintage 2028 Virginia Tech: Vick to Woodside, 25 yards, pressure in the building, no panic in the throw. It was not just the winning touchdown. It was the season's thesis statement in one route. The Hokies can beat you with the quarterback, the record-breaking receiver, the second Heisman candidate, or the back who quietly turns a track meet into a body blow.",
            "Virginia Tech leaves the ACC Championship at 12-1, with Miami falling to 10-3 after a performance that would have won a quieter title game. The Hokies have the trophy, the playoff résumé, and now the awards narrative. Woodside should wake up as the Heisman favorite. Brownlee being in the conversation only makes the offense look more impossible. The ACC title belonged to Virginia Tech on the scoreboard, but by the time the confetti settled, the national conversation belonged to Blacksburg too.",
        ],
    },
    {
        "id": "a1",
        "slug": "woodside-turns-wake-forest-into-warning-shot",
        "type": "Dynasty Wire",
        "title": "Woodside Turns Wake Forest Into a Warning Shot",
        "dek": "Virginia Tech's 49-7 demolition of Wake Forest turned Week 12 into a warning flare before the Commonwealth Clash.",
        "author": "Commonwealth Wire Staff",
        "location": "Blacksburg, VA",
        "year": 2028,
        "week": 12,
        "featuredTeam": "Virginia Tech",
        "featuredPlayer": "Marquis Woodside",
        "tags": ["Virginia Tech", "Wake Forest", "Commonwealth Clash", "ACC"],
        "relatedArticleIds": ["a2", "a3", "a4"],
        "heroImage": "week12-hero.png",
        "heroTheme": "vt",
        "published": "2028 Week 12",
        "keyStats": [
            ("Final", "Virginia Tech 49, Wake Forest 7"),
            ("Woodside", "10 REC, 190 YDS, 4 TD"),
            ("Vick Jr.", "296 PASS YDS, 4 TD"),
            ("Hokies", "10-1, 7-1 ACC"),
        ],
        "body": [
            "Virginia Tech wanted a clean final statement before rivalry week. Marquis Woodside delivered something louder. The Hokies receiver carved Wake Forest for 10 catches, 190 yards, and four touchdowns, turning a 49-7 final into the kind of score that follows a team into every Week 13 conversation.",
            "Mike Vick Jr. kept the offense on schedule with 296 passing yards and four scores, while the Hokies piled up 489 total yards. The win pushed Virginia Tech to 10-1 overall and 7-1 in ACC play, still sitting above Virginia in the conference race.",
            "Now the frame tightens. Virginia had the week off. Virginia Tech had the fireworks. The Commonwealth Clash gets both programs with top-10 CFP stakes and a state full of message boards already overheating.",
        ],
    },
    {
        "id": "a2",
        "slug": "commonwealth-clash-preview",
        "type": "Preview",
        "title": "#10 Virginia at #6 Virginia Tech: Commonwealth Clash Preview",
        "dek": "Virginia Tech brings a three-game rivalry winning streak, ACC control, and a star quarterback into the most consequential Commonwealth Clash in years.",
        "author": "Marcus Vick",
        "location": "Blacksburg, VA",
        "year": 2028,
        "week": 13,
        "featuredTeam": "Virginia Tech",
        "featuredPlayer": "Mike Vick Jr.",
        "tags": ["Commonwealth Clash", "Virginia", "Virginia Tech", "CFP"],
        "relatedArticleIds": ["a1", "a3", "a5"],
        "heroImage": "",
        "heroTheme": "split",
        "published": "2028 Week 13",
        "actionImages": [
            {
                "name": "Mike Vick Jr.",
                "team": "Virginia Tech",
                "image": "assets/action/mike-vick-jr-rollout.jpg",
                "caption": "Vick Jr.'s left-handed rollout game forces Virginia to defend beyond the pocket.",
            },
            {
                "name": "Devante Sampson",
                "team": "Virginia",
                "image": "assets/action/devante-sampson-pocket.jpg",
                "caption": "Sampson's best answer is rhythm, protection and decisive pocket passing.",
            },
        ],
        "playerImages": [
            {
                "name": "Mike Vick Jr.",
                "team": "Virginia Tech",
                "image": "assets/players/mike-vick-jr.png",
                "rating": "91 OVR",
                "style": "Left-handed dual threat",
                "stats": "295-416 (70%), 3,892 YDS, 44 TD, 15 INT",
            },
            {
                "name": "Devante Sampson",
                "team": "Virginia",
                "image": "assets/players/devante-sampson.png",
                "rating": "84 OVR",
                "style": "6-foot-6 right-handed pocket passer",
                "stats": "235-362 (64%), 2,932 YDS, 25 TD, 8 INT",
            },
        ],
        "keyStats": [
            ("Matchup", "#10 Virginia at #6 Virginia Tech"),
            ("Records", "VT 10-1, UVA 9-2"),
            ("ACC", "VT 7-1, UVA 6-2"),
            ("Series Streak", "Virginia Tech won the last 3 meetings"),
            ("Fake Spread", "Virginia Tech -4.5"),
        ],
        "body": [
            "The Commonwealth Clash has rarely needed help feeling large. This time the standings, the playoff committee and recent history all do the amplifying. Virginia Tech enters at 10-1, first in the ACC and sixth in the CFP rankings. Virginia arrives rested at 9-2, second in the conference and tenth in the playoff ranking. The winner gets state control; the result may also redraw the ACC title and CFP pictures.",
            "Virginia Tech also owns the weight that matters most in a rivalry: the Hokies have won the last three meetings. That streak gives the home side confidence, but it also raises the cost of this game. A fourth straight win would turn a good run into control of the series. A Virginia breakthrough in Blacksburg would erase three years of frustration in one night and arrive with championship consequences attached.",
            "The central contrast is at quarterback. Mike Vick Jr. is the 91-overall engine of a Virginia Tech attack that wants to stretch the field and punish hesitation. The left-handed dual threat has completed 70 percent of his passes for 3,892 yards, 44 touchdowns and 15 interceptions. His movement changes the geometry even when he stays behind the line: edge defenders must account for him, and that extra beat creates room for vertical routes.",
            "Devante Sampson gives Virginia a different silhouette. The 6-foot-6 pocket passer has completed 235 of 362 throws for 2,932 yards, 25 touchdowns and eight interceptions. His profile points toward timing, structure and winning from a firm platform. Virginia does not need Sampson to imitate Vick. It needs him to protect possessions, punish pressure and make the Hokies defend the full width of the field.",
            "Recent form favors the home side. Virginia Tech just buried Wake Forest 49-7 while producing 489 yards, including 404 through the air. Vick threw for 296 yards and four touchdowns, and Marquis Woodside detonated for 10 catches, 190 yards and four scores. For the season, Woodside has 82 catches for 1,395 yards and 20 touchdowns. Virginia cannot treat him like one dangerous receiver among several; every coverage plan has to begin with where he is aligned.",
            "The first tactical question is whether Virginia can pressure Vick without exposing its secondary. A four-man rush lets the Cavaliers keep numbers over Woodside, but it gives Vick space to extend plays. Sending extra rushers can speed up his clock, yet every blitzer removes a defender from the scramble lanes and coverage shell. Virginia has to change the picture after the snap instead of declaring one answer all night.",
            "Virginia's countermove is pace control. H. Sanders enters with 914 rushing yards and 12 touchdowns, while D. Lowell has supplied 796 receiving yards and nine scores. A steady run game and Sampson's pocket passing can shorten the night, keep Vick on the sideline and force Virginia Tech to execute against longer fields. The Cavaliers' bye week matters most if it produces answers on third down and in the red zone.",
            "That makes early-down efficiency the hidden hinge. If Sanders consistently creates second-and-manageable, Virginia can use play action, protect Sampson and keep the crowd from dictating the tempo. If the Hokies win first down and force obvious passing situations, their pass rush can attack a stationary target while the offense waits for another short field.",
            "Special teams and turnovers are the equalizers. Virginia Tech's explosiveness makes a long field survivable; Virginia cannot afford to donate extra possessions or allow a return to tilt the stadium. The Hokies, meanwhile, have to resist hunting the knockout throw when a patient drive would keep the Cavaliers chasing. In a rivalry with this much emotion, the team that accepts the boring play may be the team still composed in the fourth quarter.",
            "For Virginia Tech, the clean path is an early lead. Make Virginia abandon balance, turn the pass rush loose and let Vick attack a defense that can no longer disguise its intentions. For Virginia, the formula is almost the inverse: prevent explosive plays, tackle Woodside immediately and drag the game into a one-possession fourth quarter.",
            "The emotional math leans the same way as the football math. Virginia Tech has the three-game series streak, the hotter offense and a home crowd expecting the rivalry to remain in Hokies hands. Virginia has the rest advantage and the freedom of a road underdog, but it must survive the opening surge before those advantages can matter.",
            "Commonwealth Wire prediction: Virginia Tech 34, Virginia 27. The Hokies have the more explosive quarterback, the hotter passing game, home field and proof they know how to finish this matchup. Virginia has enough structure, rest and rivalry volatility to keep the fake spread at Virginia Tech -4.5 and every remote in the Commonwealth occupied until the final drive.",
        ],
    },
    {
        "id": "a3",
        "slug": "state-of-the-commonwealth-week-13",
        "type": "State of the Commonwealth",
        "title": "Hokies First, Hoos Second, and the State Is on Fire",
        "dek": "The ACC table has gone full rivalry mode with Virginia Tech first and Virginia second entering Week 13.",
        "author": "Commonwealth Wire Staff",
        "location": "Richmond, VA",
        "year": 2028,
        "week": 13,
        "featuredTeam": "Virginia Tech",
        "featuredPlayer": "",
        "tags": ["ACC", "Virginia", "Virginia Tech"],
        "relatedArticleIds": ["a2", "a4", "a6"],
        "heroImage": "",
        "heroTheme": "commonwealth",
        "published": "2028 Week 13",
        "keyStats": [
            ("ACC Rank", "1. Virginia Tech, 2. Virginia"),
            ("CFP", "VT #6, UVA #10"),
            ("VT Last Game", "Beat Wake Forest 49-7"),
            ("UVA Last Week", "Bye"),
        ],
        "body": [
            "The ACC table has done the rivalry a favor. Virginia Tech is not just good. Virginia is not just lurking. They are first and second in the league, separated by one conference game and a decade's worth of family bragging rights compressed into four quarters.",
            "Virginia Tech owns the momentum after the Wake Forest blowout. Virginia owns the rest advantage after the bye. That gives Week 13 a clean split: the Hokies bring proof of concept, the Cavaliers bring preparation.",
            "For now, the state line is simple. Blacksburg has the ranking edge, Charlottesville has the chance to take it, and the Commonwealth has the rare rivalry week where the standings are every bit as personal as the scoreboard.",
        ],
    },
    {
        "id": "a4",
        "slug": "message-board-meltdown-week-13",
        "type": "Message Board Meltdown",
        "title": "Wake Forest Got the Trailer, Virginia Gets the Movie",
        "dek": "The blowout sent rivalry discourse into orbit before the Cavaliers even left the bye week.",
        "author": "Commonwealth Wire Staff",
        "location": "The Internet",
        "year": 2028,
        "week": 13,
        "featuredTeam": "Virginia Tech",
        "featuredPlayer": "Marquis Woodside",
        "tags": ["Fans", "Rivalry", "Message Boards"],
        "relatedArticleIds": ["a1", "a2", "a3"],
        "heroImage": "",
        "heroTheme": "meltdown",
        "published": "2028 Week 13",
        "keyStats": [
            ("Meltdown Level", "93%"),
            ("Loudest Take", "Virginia Tech revealed nothing and everything"),
            ("Thread Count", "Unhealthy"),
            ("Next Trigger", "First UVA touchdown"),
        ],
        "body": [
            "By the fourth Woodside touchdown, the posts were already writing themselves. Hokies fans saw a contender rounding into shape. Cavaliers fans saw a Wake Forest defense that may or may not have remembered the game had started. Everybody saw rivalry week get louder.",
            "The best message-board argument is obvious: did Virginia Tech reveal too much, or did the Hokies just show Virginia exactly what it cannot stop? The bye-week crowd in Charlottesville will say preparation matters more than style points. The Blacksburg side will say 49-7 is its own scouting report.",
            "Either way, the discourse has left reasonable airspace. Welcome to the final week before the Commonwealth Clash, where every stat is evidence and every highlight is apparently a legal filing.",
        ],
    },
    {
        "id": "a5",
        "slug": "recruiting-rumor-mill-pitch-war",
        "type": "Recruiting Rumor Mill",
        "title": "The Bye Week Before the Pitch War",
        "dek": "Virginia sells preparation. Virginia Tech sells fireworks. Recruits get the full rivalry treatment.",
        "author": "Commonwealth Wire Staff",
        "location": "Recruiting HQ",
        "year": 2028,
        "week": 13,
        "featuredTeam": "Virginia Tech",
        "featuredPlayer": "",
        "tags": ["Recruiting", "Virginia", "Virginia Tech"],
        "relatedArticleIds": ["a2", "a3", "a6"],
        "heroImage": "",
        "heroTheme": "recruiting",
        "published": "2028 Week 13",
        "keyStats": [
            ("Momentum", "Virginia Tech 86, Virginia 79"),
            ("Flip Watch", "High after rivalry week"),
            ("Pipeline", "Virginia Tidewater and NOVA"),
            ("Visit Buzz", "Rivalry weekend showcase"),
        ],
        "body": [
            "Recruiting weeks like this are not quiet, even when one team is on a bye. Virginia gets to sell rest, control, and a rivalry plan. Virginia Tech gets to sell a 42-point win, a top-six ranking, and an offense that just turned a receiver into a national award headline.",
            "The Commonwealth Clash now becomes a living brochure. Every touchdown, sideline shot, and fourth-quarter camera pan can become part of the next pitch to a four-star deciding whether the state belongs to maroon or blue.",
            "No specific recruiting board is settled yet, but the stakes are obvious. The winner does not just get a scoreboard. It gets a week of screenshots, clips, and confident texts to every recruit still pretending they have not picked a favorite.",
        ],
    },
    {
        "id": "a6",
        "slug": "film-room-vick-woodside-connection",
        "type": "Film Room",
        "title": "Film Room: Why the Vick-to-Woodside Connection Changes the Math",
        "dek": "Wake Forest could not bracket, blitz, or survive the Hokies' most explosive passing concept.",
        "author": "Commonwealth Wire Film Desk",
        "location": "Blacksburg, VA",
        "year": 2028,
        "week": 13,
        "featuredTeam": "Virginia Tech",
        "featuredPlayer": "Mike Vick Jr.",
        "tags": ["Film Room", "Heisman", "Offense"],
        "relatedArticleIds": ["a1", "a2", "a5"],
        "heroImage": "",
        "heroTheme": "film",
        "published": "2028 Week 13",
        "keyStats": [
            ("Woodside", "4 receiving TD"),
            ("Vick Jr.", "44 season TD"),
            ("Explosive Plays", "Placeholder until charting"),
            ("Virginia Concern", "One-on-one coverage"),
        ],
        "body": [
            "Virginia Tech's best offensive argument is no longer just volume. It is stress. When Vick Jr. finds Woodside early, safeties stop playing downhill and the Hokies' ordinary downs start looking like scoring chances.",
            "Wake Forest had no clean answer. Soft coverage gave up rhythm throws. Pressure left Woodside isolated. By the time the fourth touchdown landed, the film had become less about Wake Forest and more about what Virginia has to solve in Week 13.",
            "The Cavaliers do have the bye-week advantage, but they cannot let the game become a track meet. If Woodside wins the first quarter, Virginia Tech can make the rest of the night feel uphill.",
        ],
    },
]

article_by_id = {article["id"]: article for article in articles}

standings = [
    ("1", "Virginia Tech", "13-1", "CFP Semifinal", "W1", 539, 288, "+251", "#3 CFP", "W 45-28 vs Penn State", "CFP Semifinal"),
    ("2", "Miami", "10-3", "ACC runner-up", "L1", 442, 309, "+133", "Bubble", "L 58-55 vs Virginia Tech", "Bowl"),
    ("3", "Virginia", "9-3", "6-3", "L1", 351, 229, "+122", "Top-25", "L at Virginia Tech", "Bowl"),
    ("4", "Georgia Tech", "8-3", "6-3", "W1", 332, 266, "+66", "#21", "W vs NC State", "Bowl"),
    ("5", "Clemson", "8-3", "5-3", "L1", 348, 238, "+110", "NR", "L vs Florida State", "Bowl"),
    ("6", "Florida State", "7-4", "5-3", "W1", 321, 275, "+46", "NR", "W vs Clemson", "Bowl"),
    ("7", "Louisville", "7-4", "4-4", "W1", 316, 284, "+32", "NR", "W vs Pitt", "Bowl"),
    ("8", "North Carolina", "6-5", "4-4", "L2", 301, 296, "+5", "NR", "L vs NC State", "vs Duke"),
    ("9", "NC State", "6-5", "3-5", "W1", 289, 302, "-13", "NR", "W vs North Carolina", "vs ECU"),
    ("10", "Penn State", "11-2", "Big Ten", "L1", 389, 341, "+48", "Eliminated", "L 45-28 vs Virginia Tech", "Season over"),
]

national_snapshot = [
    ("#1", "Texas", "CFP QF Winner", "SEC", "Cotton Bowl victor — CFP Semifinal bound"),
    ("#2", "USC", "CFP QF Winner", "Big Ten", "Rose Bowl victor — CFP Semifinal bound"),
    ("#3", "Virginia Tech", "CFP QF Winner", "ACC", "Orange Bowl: 45-28 over Penn State — Semifinal bound"),
    ("#4", "Ole Miss", "CFP QF Winner", "SEC", "Goodyear Bowl victor — CFP Semifinal bound"),
]

recruit_battles = [
    ("Caleb Ricks", "QB", "5", "Norfolk, VA", "Virginia Tech", "Warm", "Hot", "Uncommitted", "CFP run making VT irresistible."),
    ("Malik Benton", "WR", "4", "Richmond, VA", "Virginia Tech", "Hot", "Warm", "Flip watch", "Woodside's Heisman is the pitch."),
    ("Andre Coles", "EDGE", "4", "Roanoke, VA", "Virginia", "Warm", "Hot", "Uncommitted", "UVA staff selling early playing time."),
    ("Treyon Bell", "CB", "4", "Virginia Beach, VA", "Even", "Hot", "Hot", "Uncommitted", "Both teams need secondary depth."),
    ("Darius McNeil", "OT", "3", "Alexandria, VA", "Virginia Tech", "Hot", "Cool", "Committed VT", "Hokies locked the door."),
]

def esc(value):
    return html.escape(str(value), quote=True)

def rel(depth):
    return "../" * depth

def bottom_nav(depth=0, active="Home"):
    root = rel(depth)
    tabs = [
        ("Home", f"{root}index.html", "⚡"),
        ("Wire", f"{root}wire/", "📰"),
        ("Scores", f"{root}scores/", "🏈"),
        ("ACC", f"{root}acc/", "📊"),
        ("Players", f"{root}players/", "🌟"),
    ]
    items = "\n".join(
        f'<a class="tab-item {"active" if label == active else ""}" href="{href}"><span class="tab-icon">{icon}</span><span class="tab-label">{label}</span></a>'
        for label, href, icon in tabs
    )
    return f'<nav class="bottom-nav" aria-label="Primary">{items}</nav>'

def nav(depth=0, active="Home"):
    root = rel(depth)
    return f"""
    <header class="masthead">
      <a class="brand" href="{root}index.html" aria-label="Commonwealth Wire home">
        <span class="network">CW</span>
        <span class="brand-text"><strong>Commonwealth Wire</strong><em>EA CFB Dynasty · 2028 ACC Champions</em></span>
      </a>
      <div class="masthead-right">
        <span class="cfp-badge">CFP Semifinal</span>
      </div>
    </header>
    """

def ticker():
    items = [
        ("🏆", "CFP SEMIFINAL", "Virginia Tech — Orange Bowl Champions"),
        ("🔥", "RECORD BROKEN", "Woodside: 29 receiving TDs — national record"),
        ("📊", "FINAL", "Virginia Tech 45, Penn State 28"),
        ("🏅", "HEISMAN", "Woodside sweeps all 5 major awards"),
        ("🎯", "VICK JR.", "ACC single-season passing yards record"),
        ("🏈", "ACC CHAMPS", "Virginia Tech 58, Miami 55 OT"),
    ]
    items_html = "".join(
        f'<span class="tick-item"><span class="tick-badge">{badge}</span><strong>{label}</strong><span>{value}</span></span>'
        for badge, label, value in items
    )
    return f'<div class="ticker-wrap"><div class="ticker-track">{items_html}{items_html}</div></div>'

def shell(title, body, depth=0, active="Home", description="Commonwealth Dynasty Hub"):
    root = rel(depth)
    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
    <title>{esc(title)} | Commonwealth Wire</title>
    <meta name="description" content="{esc(description)}">
    <meta name="theme-color" content="#630031">
    <link rel="stylesheet" href="{root}styles.css">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  </head>
  <body>
    {nav(depth, active)}
    {ticker() if depth == 0 else ""}
    <main class="page">{body}</main>
    {bottom_nav(depth, active)}
    <div class="safe-area-bottom"></div>
  </body>
</html>
"""

def article_card(article, depth=0, size=""):
    root = rel(depth)
    game_photos = article.get("gamePhotos", [])
    thumb = ""
    if game_photos:
        thumb = f'<div class="card-thumb"><img src="{root}{esc(game_photos[0]["src"])}" alt="" loading="lazy"></div>'
    elif article.get("heroImage"):
        img = article["heroImage"]
        if not img.endswith(".svg"):
            thumb = f'<div class="card-thumb"><img src="{root}{esc(img)}" alt="" loading="lazy"></div>'
    return f"""
      <a class="article-card {size}" href="{root}articles/{article['slug']}/">
        {thumb}
        <div class="card-body">
          <span class="kicker">{esc(article['type'])}</span>
          <strong>{esc(article['title'])}</strong>
          <em>{esc(article['dek'])}</em>
        </div>
      </a>
    """

def standings_table():
    rows = []
    for row in standings:
        team_class = " team-vt" if row[1] == "Virginia Tech" else " team-uva" if row[1] == "Virginia" else ""
        rows.append("<tr class=\"" + team_class.strip() + "\">" + "".join(f"<td>{esc(cell)}</td>" for cell in row) + "</tr>")
    return f"""
      <div class="table-wrap">
        <table class="data-table standings-table">
          <thead><tr><th>Rank</th><th>Team</th><th>Overall</th><th>ACC</th><th>Streak</th><th>PF</th><th>PA</th><th>Diff</th><th>CFP</th><th>Last Game</th><th>Next Game</th></tr></thead>
          <tbody>{''.join(rows)}</tbody>
        </table>
      </div>
    """

def recruiting_table():
    rows = []
    for row in recruit_battles:
        rows.append("<tr>" + "".join(f"<td>{esc(cell)}</td>" for cell in row) + "</tr>")
    return f"""
      <div class="table-wrap">
        <table class="data-table">
          <thead><tr><th>Recruit</th><th>Position</th><th>Stars</th><th>Hometown</th><th>Leader</th><th>VT Interest</th><th>UVA Interest</th><th>Status</th><th>Notes</th></tr></thead>
          <tbody>{''.join(rows)}</tbody>
        </table>
      </div>
    """

def national_table():
    rows = []
    for rank, team, record, league, note in national_snapshot:
        team_class = " team-vt" if team == "Virginia Tech" else " team-uva" if team == "Virginia" else ""
        rows.append(f'<tr class="{team_class.strip()}"><td>{esc(rank)}</td><td>{esc(team)}</td><td>{esc(record)}</td><td>{esc(league)}</td><td>{esc(note)}</td></tr>')
    return f"""
      <div class="table-wrap">
        <table class="data-table national-table">
          <thead><tr><th>CFP</th><th>Team</th><th>Record</th><th>League</th><th>Why It Matters</th></tr></thead>
          <tbody>{''.join(rows)}</tbody>
        </table>
      </div>
    """

def game_photo_strip(photos, depth=0):
    root = rel(depth)
    if not photos:
        return ""
    cards = []
    for p in photos:
        cards.append(f"""
          <figure class="game-photo-card">
            <img src="{root}{esc(p['src'])}" alt="{esc(p['caption'])}" loading="lazy">
            <figcaption>
              <span class="photo-label">{esc(p['label'])}</span>
              <span>{esc(p['caption'])}</span>
            </figcaption>
          </figure>""")
    return f'<div class="game-photo-strip">{"".join(cards)}</div>'

def home():
    lead = articles[0]
    body = f"""
      <section class="hero-section">
        <a class="hero-card" href="articles/{lead['slug']}/">
          <div class="hero-img-wrap">
            <img src="{esc(lead['heroImage'] or 'assets/game/orange-bowl-winner.jpg')}" alt="Virginia Tech CFP Quarterfinal win">
            <div class="hero-gradient"></div>
          </div>
          <div class="hero-copy">
            <span class="kicker-pill">{esc(lead['type'])}</span>
            <h1 class="hero-title">{esc(lead['title'])}</h1>
            <p class="hero-dek">{esc(lead['dek'])}</p>
            <span class="hero-byline">{esc(lead['author'])} · {esc(lead['published'])}</span>
          </div>
        </a>
      </section>

      <section class="cfp-banner">
        <div class="cfp-banner-inner">
          <span class="cfp-banner-label">🏆 CFP SEMIFINAL BOUND</span>
          <span class="cfp-banner-score">VT 45 · PSU 28</span>
          <span class="cfp-banner-sub">Woodside: 29 season TDs — National Record</span>
        </div>
      </section>

      <section class="content-section">
        <div class="section-label">Top Stories</div>
        <div class="card-feed">
          {''.join(article_card(a) for a in articles[:6])}
        </div>
      </section>

      <section class="stats-strip">
        <div class="stat-pill"><span class="stat-val">13-1</span><span class="stat-lbl">Record</span></div>
        <div class="stat-pill"><span class="stat-val">#3</span><span class="stat-lbl">CFP Seed</span></div>
        <div class="stat-pill highlight"><span class="stat-val">29</span><span class="stat-lbl">Woodside TDs</span></div>
        <div class="stat-pill"><span class="stat-val">45</span><span class="stat-lbl">OB Points</span></div>
        <div class="stat-pill"><span class="stat-val">ACC</span><span class="stat-lbl">Champions</span></div>
      </section>

      <section class="content-section">
        <div class="section-label">Season Snapshot</div>
        <div class="snapshot-grid">
          <div class="snap-card vt"><span>ACC Champions</span><strong>Virginia Tech</strong><p>58-55 OT over Miami. Woodside's 4 TDs in Charlotte.</p></div>
          <div class="snap-card"><span>Heisman</span><strong>Marquis Woodside</strong><p>5 awards. National TD record. Freshman.</p></div>
          <div class="snap-card"><span>Orange Bowl</span><strong>VT 45 · PSU 28</strong><p>Overton's 63-yard run. Vick sets ACC record.</p></div>
          <div class="snap-card"><span>Next Up</span><strong>CFP Semifinal</strong><p>The Hokies are four quarters from the title game.</p></div>
        </div>
      </section>
    """
    return shell("Home", body, 0, "Home")

def simple_page(title, active, intro, content):
    return shell(title, f'<section class="section-block"><div class="section-head"><span class="kicker">Commonwealth Wire</span><h1>{esc(title)}</h1><p class="intro-text">{esc(intro)}</p></div>{content}</section>', 1, active)

def article_page(article):
    root = rel(2)
    related = [article_by_id[i] for i in article["relatedArticleIds"] if i in article_by_id]
    player_images = article.get("playerImages", [])
    action_images = article.get("actionImages", [])
    game_photos = article.get("gamePhotos", [])

    # Hero
    if game_photos:
        hero_img = f'<img src="{root}{esc(game_photos[0]["src"])}" alt="{esc(article["title"])}" class="article-hero-img">'
    elif action_images:
        action_cards = []
        for action in action_images:
            team_class = "vt" if action["team"] == "Virginia Tech" else "uva"
            action_cards.append(f'''
              <figure class="action-photo {team_class}">
                <img src="{root}{esc(action['image'])}" alt="{esc(action['name'])} in game action">
                <figcaption><strong>{esc(action['name'])}</strong><span>{esc(action['caption'])}</span></figcaption>
              </figure>''')
        hero_img = '<div class="action-duel">' + ''.join(action_cards) + '</div>'
    elif article.get("heroImage") and not article["heroImage"].endswith(".svg"):
        hero_img = f'<img src="{root}{esc(article["heroImage"])}" alt="{esc(article["title"])}" class="article-hero-img">'
    elif article.get("heroImage"):
        hero_img = f'<img src="{root}{esc(article["heroImage"])}" alt="{esc(article["title"])}" class="article-hero-img">'
    else:
        hero_img = f'<div class="article-hero-placeholder {esc(article["heroTheme"])}"><span>{esc(article["type"])}</span></div>'

    profile_matchup = ""
    if player_images:
        player_cards = []
        for player in player_images:
            team_class = "vt" if player["team"] == "Virginia Tech" else "uva"
            player_cards.append(f'''
              <figure class="quarterback-card {team_class}">
                <img src="{root}{esc(player['image'])}" alt="{esc(player['name'])}">
                <figcaption><span>{esc(player['team'])} | {esc(player['rating'])}</span><strong>{esc(player['name'])}</strong><em>{esc(player['style'])}</em><p>{esc(player['stats'])}</p></figcaption>
              </figure>''')
        profile_matchup = '<section class="tale-of-tape"><span class="kicker">Quarterback Tale of the Tape</span><div class="quarterback-duel">' + ''.join(player_cards) + '</div></section>'

    stats = "".join(f"<li><strong>{esc(k)}</strong><span>{esc(v)}</span></li>" for k, v in article["keyStats"])
    body_html = "\n".join(f"<p>{esc(p)}</p>" for p in article["body"])
    related_html = "".join(article_card(a, 2) for a in related)
    photo_strip = game_photo_strip(game_photos[1:], 2) if len(game_photos) > 1 else ""

    page_body = f"""
      <article class="article-page">
        <a class="back-link" href="{root}wire/">← Dynasty Wire</a>
        <div class="article-shell">
          <main class="article-main">
            <span class="kicker">{esc(article['type'])}</span>
            <h1>{esc(article['title'])}</h1>
            <p class="dek">{esc(article['dek'])}</p>
            <div class="article-meta">{esc(article['author'])} · {esc(article['location'])} · {esc(article['published'])}</div>
            <div class="article-hero">{hero_img}</div>
            {profile_matchup}
            <div class="article-body">{body_html}</div>
            {photo_strip}
          </main>
          <aside class="article-sidebar">
            <section class="panel"><div class="panel-head tight"><h2>Key Stats</h2></div><ul class="key-stats">{stats}</ul></section>
            <section class="panel"><div class="panel-head tight"><h2>Related</h2></div><div class="feed-list small">{related_html}</div></section>
          </aside>
        </div>
      </article>
    """
    return shell(article["title"], page_body, 2, "Wire", article["dek"])

def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)

write(SITE / "index.html", home())
write(SITE / "scores" / "index.html", simple_page("Scores", "Scores", "CFP Quarterfinal final, plus the full ACC Championship run.", """
  <div class="cards-2">
    <article class="panel"><span class="kicker">CFP Quarterfinal</span><h2>Virginia Tech 45, Penn State 28</h2><p>Orange Bowl. Woodside: 9/157/3TD. Overton: 63-yard TD. Vick Jr.: 24/34, 281, 4TD. VT advances to the CFP Semifinal.</p></article>
    <article class="panel"><span class="kicker">ACC Championship</span><h2>Virginia Tech 58, Miami 55 (OT)</h2><p>VT: 612 total yards, 251 rushing yards, 361 passing yards, and 8-of-11 on third down.</p></article>
    <article class="panel"><span class="kicker">Commonwealth Clash</span><h2>Virginia Tech beat Virginia</h2><p>The Hokies handled the rivalry step, advanced to the ACC Championship, and then finished the job.</p></article>
    <article class="panel"><span class="kicker">Records</span><h2>VT 13-1 | CFP Semifinal</h2><p>Virginia Tech exits the Orange Bowl as a CFP Semifinalist with the ACC trophy in hand.</p></article>
  </div>
"""))
write(SITE / "acc" / "index.html", simple_page("ACC Standings", "ACC", "Virginia Tech's 13-1 run through the ACC and into the CFP Semifinal.", standings_table() + """
  <div class="cards-2 section-spacer">
    <article class="panel title-race"><span class="kicker">CFP Semifinal</span><h2>Virginia Tech Advanced</h2><p>Orange Bowl: 45-28 over Penn State. The Hokies are in the final four.</p></article>
    <article class="panel"><span class="kicker">Next Up</span><h2>CFP Semifinal bracket</h2><p>#3 VT faces the winner from the other bracket. Texas, USC, and Ole Miss are all in.</p></article>
  </div>
  <section class="section-spacer"><div class="panel-head"><h2>CFP Final Four</h2></div>""" + national_table() + """</section>
"""))
write(SITE / "players" / "index.html", simple_page("Impact Players", "Players", "Players who built Virginia Tech's ACC Championship and CFP run.", """
  <div class="cards-3">
    <article class="panel player-card"><span>WR | Virginia Tech</span><h2>Marquis Woodside</h2><p>Heisman. Biletnikoff. Maxwell. Walter Camp. Shaun Alexander Award. 29 receiving TDs — national record. And still a freshman.</p></article>
    <article class="panel player-card featured-player"><img src="../assets/players/mike-vick-jr.png" alt="Mike Vick Jr."><span>QB | Virginia Tech | 91 OVR</span><h2>Mike Vick Jr.</h2><p>ACC single-season passing yards record. Orange Bowl: 24-34, 281 YDS, 4 TD. Championship: 22-29, 361 YDS, 5 TD.</p></article>
    <article class="panel player-card"><span>WR | Virginia Tech</span><h2>Nick Brownlee</h2><p>7 catches, 65 yards in the Orange Bowl. A Heisman-race presence who makes the whole offense harder to defend.</p></article>
    <article class="panel player-card"><span>RB | Virginia Tech</span><h2>Jeff Overton</h2><p>63-yard run in the Orange Bowl's fourth quarter that sealed the win. 131 yards, 11.9 YPC on 11 carries.</p></article>
    <article class="panel player-card"><span>S | Virginia Tech</span><h2>Doug Bulluck</h2><p>51-yard interception return in Q2 of the Orange Bowl. The play that turned a close game into a Hokie rout.</p></article>
    <article class="panel player-card"><span>Miami</span><h2>DeMarco Hodges</h2><p>81-yard touchdown in the ACC Championship. Miami could not stay in it, but Hodges made the night feel dangerous.</p></article>
  </div>
"""))
write(SITE / "recruiting" / "index.html", simple_page("Recruiting HQ", "Recruiting", "The Heisman and a CFP run have changed the Commonwealth recruiting map.", f"""
  <div class="cards-3">
    <article class="panel"><span class="kicker">Momentum Score</span><h2>VT 95 | UVA 71</h2><p>Woodside's Heisman and a CFP Semifinal berth have tilted the board hard toward Blacksburg.</p></article>
    <article class="panel"><span class="kicker">Flip Watch</span><h2>Receivers are calling</h2><p>Every WR recruit in the country knows what playing for Vick Jr. means. The pitch writes itself.</p></article>
    <article class="panel"><span class="kicker">Visit Buzz</span><h2>CFP = Recruiting Weekend</h2><p>Top targets want to see Blacksburg electric. The Hokies are delivering.</p></article>
  </div>
  <section class="section-spacer"><div class="panel-head"><h2>Head-to-Head Recruiting Battles</h2></div>{recruiting_table()}</section>
"""))
write(SITE / "wire" / "index.html", simple_page("Dynasty Wire", "Wire", "News, recaps, and features from the 2028 season.", '<div class="card-feed">' + "".join(article_card(a, 1) for a in articles) + "</div>"))
write(SITE / "clash" / "index.html", simple_page("Commonwealth Clash", "Home", "Virginia Tech beat Virginia, then carried that momentum to the ACC Championship.", f"""
  <div class="cards-2">
    <article class="panel"><span class="kicker">Result</span><h2>Virginia Tech beat Virginia</h2><p>The Hokies extended the rivalry streak and punched the Charlotte ticket.</p></article>
    <article class="panel"><span class="kicker">Aftermath</span><h2>ACC Championship → CFP</h2><p>VT beat Miami 58-55 in overtime, then Penn State 45-28 in the Orange Bowl.</p></article>
  </div>
"""))
write(SITE / "records" / "index.html", simple_page("Record Watch", "Home", "The 2028 season broke records at every level.", """
  <div class="cards-3">
    <article class="panel record-card"><strong>National Record</strong><span>Marquis Woodside — 29 receiving TDs in a season. Broke the national all-time record set by Bailey Zappe in 2021.</span></article>
    <article class="panel record-card"><strong>ACC Record</strong><span>Mike Vick Jr. — ACC single-season passing yards. Set in the Capital One Orange Bowl vs Penn State.</span></article>
    <article class="panel record-card"><strong>ACC Record</strong><span>Woodside — ACC single-season receiving yards (set during regular season, before the Orange Bowl).</span></article>
  </div>
"""))
for article in articles:
    write(SITE / "articles" / article["slug"] / "index.html", article_page(article))

DATA.mkdir(parents=True, exist_ok=True)
(DATA / "articles.json").write_text(json.dumps(articles, indent=2, default=str))

print(f"Built {len(articles)} articles and static pages in {SITE}")
