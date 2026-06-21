from pathlib import Path
import json
import html

SITE = Path(__file__).resolve().parent
DATA = SITE.parent / "data"

articles = [
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
    ("1", "Virginia Tech", "10-1", "7-1", "W3", 436, 205, "+231", "#6", "W 49-7 vs Wake Forest", "vs #10 Virginia"),
    ("2", "Virginia", "9-2", "6-2", "BYE", 351, 229, "+122", "#10", "Bye", "at #6 Virginia Tech"),
    ("3", "Miami", "9-2", "6-2", "W2", 387, 251, "+136", "#13", "W vs Duke", "vs Boston College"),
    ("4", "Georgia Tech", "8-3", "6-3", "W1", 332, 266, "+66", "#21", "W vs NC State", "Regular season complete"),
    ("5", "Clemson", "8-3", "5-3", "L1", 348, 238, "+110", "NR", "L vs Florida State", "at South Carolina"),
    ("6", "Florida State", "7-4", "5-3", "W1", 321, 275, "+46", "NR", "W vs Clemson", "vs Florida"),
    ("7", "Louisville", "7-4", "4-4", "W1", 316, 284, "+32", "NR", "W vs Pitt", "at Kentucky"),
    ("8", "North Carolina", "6-5", "4-4", "L2", 301, 296, "+5", "NR", "L vs NC State", "vs Duke"),
    ("9", "NC State", "6-5", "3-5", "W1", 289, 302, "-13", "NR", "W vs North Carolina", "vs ECU"),
    ("10", "Duke", "5-6", "3-5", "L1", 265, 311, "-46", "NR", "L vs Miami", "at North Carolina"),
    ("11", "Wake Forest", "4-7", "2-6", "L3", 244, 354, "-110", "NR", "L 49-7 at Virginia Tech", "vs Syracuse"),
    ("12", "Pitt", "4-7", "2-6", "L2", 251, 329, "-78", "NR", "L vs Louisville", "at West Virginia"),
]

national_snapshot = [
    ("#1", "Ohio State", "11-0", "Big Ten", "Unbeaten front-runner"),
    ("#2", "USC", "11-0", "Big Ten", "Track-meet offense, playoff lock pace"),
    ("#3", "Texas", "10-1", "SEC", "One-loss power still in the top tier"),
    ("#4", "Oregon", "10-1", "Big Ten", "Explosive profile keeps CFP pressure high"),
    ("#5", "Georgia", "10-1", "SEC", "Still lurking near the top line"),
    ("#6", "Virginia Tech", "10-1", "ACC", "Commonwealth Clash can lock in the narrative"),
    ("#10", "Virginia", "9-2", "ACC", "Road upset would shake the CFP bubble"),
]

recruit_battles = [
    ("Caleb Ricks", "QB", "5", "Norfolk, VA", "Virginia Tech", "Warm", "Hot", "Uncommitted", "Rivalry visit could swing the board."),
    ("Malik Benton", "WR", "4", "Richmond, VA", "Virginia Tech", "Hot", "Warm", "Flip watch", "Woodside's award week is now part of the pitch."),
    ("Andre Coles", "EDGE", "4", "Roanoke, VA", "Virginia", "Warm", "Hot", "Uncommitted", "UVA staff selling early playing time."),
    ("Treyon Bell", "CB", "4", "Virginia Beach, VA", "Even", "Hot", "Hot", "Uncommitted", "Both teams need secondary depth."),
    ("Darius McNeil", "OT", "3", "Alexandria, VA", "Virginia Tech", "Hot", "Cool", "Committed VT", "Hokies trying to lock the door."),
]

def esc(value):
    return html.escape(str(value), quote=True)

def rel(depth):
    return "../" * depth

def nav(depth=0, active="Home"):
    root = rel(depth)
    links = [
        ("Home", f"{root}index.html"),
        ("Scores", f"{root}scores/"),
        ("ACC", f"{root}acc/"),
        ("Players", f"{root}players/"),
        ("Recruiting", f"{root}recruiting/"),
        ("Dynasty Wire", f"{root}wire/"),
        ("Commonwealth Clash", f"{root}clash/"),
        ("Records", f"{root}records/"),
    ]
    items = "\n".join(f'<a class="{"active" if label == active else ""}" href="{href}">{label}</a>' for label, href in links)
    return f"""
    <header class="masthead">
      <a class="brand" href="{root}index.html" aria-label="Commonwealth Wire home">
        <span class="network">CW</span>
        <span><strong>Commonwealth Wire</strong><em>EA College Football Dynasty | 2028 Week 13</em></span>
      </a>
      <nav aria-label="Primary">{items}</nav>
    </header>
    """

def ticker():
    return """
    <section class="scorebar" id="scores">
      <a class="scorebox final" href="scores/"><span>Final</span><strong>Virginia Tech 49</strong><em>Wake Forest 7</em></a>
      <a class="scorebox" href="scores/"><span>Bye</span><strong>Virginia</strong><em>9-2 | #10 CFP</em></a>
      <a class="scorebox live" href="clash/"><span>Next</span><strong>#10 Virginia at #6 Virginia Tech</strong><em>Commonwealth Clash</em></a>
      <a class="scorebox" href="acc/"><span>ACC</span><strong>1. VT | 2. UVA</strong><em>Title race pressure</em></a>
    </section>
    """

def shell(title, body, depth=0, active="Home", description="Commonwealth Dynasty Hub"):
    root = rel(depth)
    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{esc(title)} | Commonwealth Wire</title>
    <meta name="description" content="{esc(description)}">
    <link rel="stylesheet" href="{root}styles.css">
  </head>
  <body>
    {nav(depth, active)}
    {ticker() if depth == 0 else ""}
    <main class="page">{body}</main>
  </body>
</html>
"""

def article_card(article, depth=0, size=""):
    root = rel(depth)
    return f"""
      <a class="article-card {size}" href="{root}articles/{article['slug']}/">
        <span class="kicker">{esc(article['type'])}</span>
        <strong>{esc(article['title'])}</strong>
        <em>{esc(article['dek'])}</em>
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

def module_grid():
    modules = [
        ("Stock Up", "Virginia Tech explosiveness, Woodside's award case, rivalry-week ticket prices."),
        ("Stock Down", "Wake Forest's fourth-quarter tape and every defensive coordinator facing the Hokies."),
        ("Message Board Meltdown", "Confidence is no longer a mood. It is a spreadsheet with caps lock."),
        ("Film Room", "Vick Jr. to Woodside forces Virginia to pick between pressure and brackets."),
        ("Coach Hot Seat", "No real flames yet, but one rivalry collapse will create pretend smoke."),
        ("CFP Bubble Watch", "Virginia Tech controls the better lane. Virginia can crash it with one road win."),
        ("Rivalry Trophy Tracker", "The Commonwealth Clash is currently in pressure-cooker mode."),
        ("Fan Confidence Meter", "Hokies 91%, Cavaliers 74%, neutral fans 100% entertained."),
    ]
    return '<div class="module-grid">' + "".join(f'<article class="mini-module"><span>{esc(t)}</span><p>{esc(b)}</p></article>' for t, b in modules) + "</div>"

def home():
    lead = articles[1]
    body = f"""
      <section class="hero-layout">
        <a class="hero-card" href="articles/{lead['slug']}/">
          <img src="assets/action/mike-vick-jr-rollout.jpg" alt="Mike Vick Jr. leads Virginia Tech into the Commonwealth Clash">
          <span class="hero-copy">
            <span class="kicker">Top Story</span>
            <span class="hero-title">{esc(lead['title'])}</span>
            <span class="hero-dek">{esc(lead['dek'])}</span>
            <span class="byline">{esc(lead['author'])} | Week 13</span>
          </span>
        </a>
        <aside class="headline-stack">
          {article_card(articles[0])}
          {article_card(articles[2])}
          {article_card(articles[5])}
        </aside>
      </section>

      <section class="section-block clash-center">
        <div class="section-head">
          <span class="kicker">Week 13</span>
          <h1>Commonwealth Clash Preview Center</h1>
          <p>#10 Virginia visits #6 Virginia Tech with the ACC title race, CFP positioning, and state bragging rights all pressed into one rivalry night.</p>
        </div>
        <div class="preview-grid">
          <article><span>Matchup</span><strong>#10 Virginia at #6 Virginia Tech</strong><p>Virginia comes off a bye. Virginia Tech comes off a 49-7 statement.</p></article>
          <article><span>Stakes</span><strong>ACC race, CFP leverage, state control</strong><p>The winner owns the cleanest Commonwealth narrative entering the postseason.</p></article>
          <article><span>QB Matchup</span><strong>Mike Vick Jr. vs Devante Sampson</strong><p>Vick has the Heisman noise. Sampson has the chance to steal the week.</p></article>
          <article><span>X-Factor</span><strong>Marquis Woodside</strong><p>After 10 catches, 190 yards, and 4 TD, every coverage call starts with him.</p></article>
          <article><span>VT Needs</span><strong>Start fast, force Virginia to chase</strong><p>Make the bye-week script irrelevant by winning the first two drives.</p></article>
          <article><span>UVA Needs</span><strong>Shorten the game and hit explosives</strong><p>Keep Vick Jr. off rhythm and make the fourth quarter uncomfortable.</p></article>
          <article><span>Fake Spread</span><strong>Virginia Tech -4.5</strong><p>Prediction desk leans Hokies 34-27, with upset volatility very much alive.</p></article>
          <article><span>State of the Commonwealth</span><strong>The state has receipts ready</strong><p>One family rivalry, one ACC race, and one week of screenshots waiting.</p></article>
        </div>
        <div class="home-qb-duel" aria-label="Quarterback matchup">
          <article class="qb-panel vt">
            <img src="assets/action/mike-vick-jr-rollout.jpg" alt="Mike Vick Jr. rolling left to pass for Virginia Tech">
            <div><span>Virginia Tech | 91 OVR</span><strong>Mike Vick Jr.</strong><p>Left-handed dual threat | 3,892 YDS | 44 TD | 15 INT</p></div>
          </article>
          <div class="versus-mark"><span>QB Matchup</span><strong>VS</strong><em>Explosive creation meets pocket control</em></div>
          <article class="qb-panel uva">
            <img src="assets/action/devante-sampson-pocket.jpg" alt="Devante Sampson passing from the pocket for Virginia">
            <div><span>Virginia | 84 OVR</span><strong>Devante Sampson</strong><p>6-foot-6 pocket passer | 2,932 YDS | 25 TD | 8 INT</p></div>
          </article>
        </div>
        <a class="button-link" href="articles/commonwealth-clash-preview/">Read the full preview</a>
      </section>

      <section class="dashboard-grid">
        <div class="main-column">
          <section class="panel">
            <div class="panel-head"><h2>Latest Scores</h2><a href="scores/">Full scoreboard</a></div>
            <div class="score-summary"><strong>Virginia Tech 49</strong><span>Wake Forest 7</span><em>Final | Week 12</em></div>
            <div class="score-summary muted"><strong>Virginia</strong><span>Bye</span><em>9-2 | #10 CFP</em></div>
          </section>

          <section class="panel">
            <div class="panel-head"><h2>Dynasty Wire</h2><a href="wire/">All articles</a></div>
            <div class="feed-list">{''.join(article_card(a) for a in articles[1:6])}</div>
          </section>

          <section class="panel">
            <div class="panel-head"><h2>Creative Desk</h2><span>Generated modules</span></div>
            {module_grid()}
          </section>
        </div>

        <aside class="side-column">
          <section class="panel">
            <div class="panel-head tight"><h2>ACC Snapshot</h2><a href="acc/">Table</a></div>
            <ol class="rank-list"><li><strong>Virginia Tech</strong><span>10-1 | 7-1 | #6</span></li><li><strong>Virginia</strong><span>9-2 | 6-2 | #10</span></li><li><strong>Miami</strong><span>9-2 | 6-2 | #13</span></li><li><strong>Georgia Tech</strong><span>8-3 | 6-3 | #21</span></li></ol>
          </section>
          <section class="panel">
            <div class="panel-head tight"><h2>CFP Top Teams</h2><a href="acc/">Context</a></div>
            <ol class="rank-list"><li><strong>#1 Ohio State</strong><span>11-0</span></li><li><strong>#2 USC</strong><span>11-0</span></li><li><strong>#6 Virginia Tech</strong><span>10-1</span></li><li><strong>#10 Virginia</strong><span>9-2</span></li></ol>
          </section>
          <section class="panel">
            <div class="panel-head tight"><h2>Heisman Watch</h2></div>
            <div class="spotlight"><span>QB | Virginia Tech</span><strong>Mike Vick Jr.</strong><p>3,892 passing yards, 44 TD, 15 INT. Week 12: 296 yards, 4 TD.</p></div>
          </section>
          <section class="panel">
            <div class="panel-head tight"><h2>Recruiting Buzz</h2><a href="recruiting/">HQ</a></div>
            <p>Rivalry weekend is now a recruiting event. Virginia Tech has momentum, Virginia has the bye-week pitch, and every in-state target gets a new sales deck.</p>
          </section>
          <section class="panel">
            <div class="panel-head tight"><h2>Record Watch</h2></div>
            <div class="record-row"><strong>4</strong><span>Woodside receiving TD vs Wake Forest</span></div>
            <div class="record-row"><strong>190</strong><span>Woodside receiving yards vs Wake Forest</span></div>
          </section>
        </aside>
      </section>
    """
    return shell("Home", body, 0, "Home")

def simple_page(title, active, intro, content):
    return shell(title, f'<section class="section-block"><div class="section-head"><span class="kicker">Commonwealth Wire</span><h1>{esc(title)}</h1><p>{esc(intro)}</p></div>{content}</section>', 1, active)

def article_page(article):
    root = rel(2)
    related = [article_by_id[i] for i in article["relatedArticleIds"] if i in article_by_id]
    player_images = article.get("playerImages", [])
    action_images = article.get("actionImages", [])
    profile_matchup = ""
    if player_images:
        player_cards = []
        for player in player_images:
            team_class = "vt" if player["team"] == "Virginia Tech" else "uva"
            player_cards.append(f'''
              <figure class="quarterback-card {team_class}">
                <img src="{root}{esc(player['image'])}" alt="{esc(player['name'])} {esc(player['team'])} player card">
                <figcaption><span>{esc(player['team'])} | {esc(player['rating'])}</span><strong>{esc(player['name'])}</strong><em>{esc(player['style'])}</em><p>{esc(player['stats'])}</p></figcaption>
              </figure>''')
        profile_matchup = '<section class="tale-of-tape"><span class="kicker">Quarterback Tale of the Tape</span><div class="quarterback-duel">' + ''.join(player_cards) + '</div></section>'
    if action_images:
        action_cards = []
        for action in action_images:
            team_class = "vt" if action["team"] == "Virginia Tech" else "uva"
            action_cards.append(f'''
              <figure class="action-photo {team_class}">
                <img src="{root}{esc(action['image'])}" alt="{esc(action['name'])} in game action for {esc(action['team'])}">
                <figcaption><strong>{esc(action['name'])}</strong><span>{esc(action['caption'])}</span></figcaption>
              </figure>''')
        hero = '<div class="action-duel">' + ''.join(action_cards) + '</div>'
    elif player_images:
        hero = profile_matchup
        profile_matchup = ""
    else:
        hero = f'<img src="{root}{article["heroImage"]}" alt="{esc(article["title"])}">' if article["heroImage"] else f'<div class="article-hero-placeholder {esc(article["heroTheme"])}"><span>{esc(article["type"])}</span></div>'
    stats = "".join(f"<li><strong>{esc(k)}</strong><span>{esc(v)}</span></li>" for k, v in article["keyStats"])
    body = "\n".join(f"<p>{esc(p)}</p>" for p in article["body"])
    related_html = "".join(article_card(a, 2) for a in related)
    profile_block = f"\n            {profile_matchup}" if profile_matchup else ""
    page_body = f"""
      <article class="article-page">
        <a class="back-link" href="{root}wire/">Back to Dynasty Wire</a>
        <div class="article-shell">
          <main class="article-main">
            <span class="kicker">{esc(article['type'])}</span>
            <h1>{esc(article['title'])}</h1>
            <p class="dek">{esc(article['dek'])}</p>
            <div class="article-meta">{esc(article['author'])} | {esc(article['location'])} | {esc(article['published'])}</div>
            <div class="article-hero">{hero}</div>{profile_block}
            <div class="article-body">{body}</div>
          </main>
          <aside class="article-sidebar">
            <section class="panel"><div class="panel-head tight"><h2>Key Stats</h2></div><ul class="key-stats">{stats}</ul></section>
            <section class="panel"><div class="panel-head tight"><h2>Related</h2></div><div class="feed-list small">{related_html}</div></section>
          </aside>
        </div>
      </article>
    """
    return shell(article["title"], page_body, 2, "Dynasty Wire", article["dek"])

def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)

write(SITE / "index.html", home())
write(SITE / "scores" / "index.html", simple_page("Scores", "Scores", "Week 12 final and Week 13 rivalry setup.", """
  <div class="cards-2">
    <article class="panel"><span class="kicker">Final</span><h2>Virginia Tech 49, Wake Forest 7</h2><p>VT: 489 total yards, 404 passing yards, 85 rushing yards, 5-8 on third down. Wake Forest: 222 total yards.</p></article>
    <article class="panel"><span class="kicker">Bye</span><h2>Virginia</h2><p>The Cavaliers rested at 9-2 overall, 6-2 ACC, and #10 CFP before traveling to Blacksburg.</p></article>
    <article class="panel"><span class="kicker">Next</span><h2>#10 Virginia at #6 Virginia Tech</h2><p>Commonwealth Clash week. ACC title race pressure, CFP pressure, and one family scoreboard.</p></article>
  </div>
"""))
write(SITE / "acc" / "index.html", simple_page("ACC Standings", "ACC", "A fuller standings table for the 2028 Week 13 title race, with national CFP context underneath.", standings_table() + """
  <div class="cards-2 section-spacer">
    <article class="panel title-race"><span class="kicker">ACC Title Race</span><h2>The Commonwealth Clash Is the Table</h2><p>Virginia Tech controls first place at 7-1 in the league. Virginia is one game back and can turn the rivalry into a conference-title argument with a road win. Miami remains close enough that every tiebreaker conversation should be treated carefully until the full schedule is final.</p></article>
    <article class="panel"><span class="kicker">Graceful Data Note</span><h2>Some league stats are placeholders</h2><p>Points for, points against, and non-rival results can be replaced once more screenshots are extracted.</p></article>
  </div>
  <section class="section-spacer"><div class="panel-head"><h2>National CFP Snapshot</h2><span>Relevant top teams</span></div>""" + national_table() + """</section>
"""))
write(SITE / "players" / "index.html", simple_page("Impact Players", "Players", "Players shaping the Week 13 rivalry story.", """
  <div class="cards-3">
    <article class="panel player-card featured-player"><img src="../assets/players/mike-vick-jr.png" alt="Mike Vick Jr. Virginia Tech player card"><span>QB | Virginia Tech | 91 OVR</span><h2>Mike Vick Jr.</h2><p>Left-handed dual threat. 3,892 season passing yards, 44 TD, 15 INT. Week 12: 296 yards, 4 TD, 1 INT.</p></article>
    <article class="panel player-card"><span>WR | Virginia Tech</span><h2>Marquis Woodside</h2><p>National Offensive Player of the Week after 10 catches, 190 yards, and 4 TD.</p></article>
    <article class="panel player-card featured-player"><img src="../assets/players/devante-sampson.png" alt="Devante Sampson Virginia player card"><span>QB | Virginia | 84 OVR</span><h2>Devante Sampson</h2><p>6-foot-6 pocket passer. 2,932 passing yards, 25 TD, 8 INT entering the Commonwealth Clash.</p></article>
    <article class="panel player-card"><span>WR | Virginia</span><h2>D. Lowell</h2><p>55 catches, 796 yards, 9 TD. A key explosive option for the Cavaliers.</p></article>
    <article class="panel player-card"><span>RB | Virginia</span><h2>H. Sanders</h2><p>173 carries, 914 rushing yards, 12 TD. Virginia's pace-control lever.</p></article>
    <article class="panel player-card"><span>WR | Virginia Tech</span><h2>B. Rowley</h2><p>84 catches, 1,272 yards, 16 TD. Another reason defenses cannot overcommit to Woodside.</p></article>
  </div>
"""))
write(SITE / "recruiting" / "index.html", simple_page("Recruiting HQ", "Recruiting", "The Commonwealth recruiting war gets a rivalry-week front page.", f"""
  <div class="cards-3">
    <article class="panel"><span class="kicker">Team Rankings</span><h2>VT: #8 class | UVA: #14 class</h2><p>Sample rankings until the next recruiting screenshots are extracted.</p></article>
    <article class="panel"><span class="kicker">Momentum Score</span><h2>VT 86 | UVA 79</h2><p>Virginia Tech has fireworks. Virginia has the bye-week pitch and playing-time angles.</p></article>
    <article class="panel"><span class="kicker">Visit Schedule</span><h2>Rivalry Weekend Showcase</h2><p>Top in-state targets are marked for virtual visit follow-up after Week 13.</p></article>
  </div>
  <section class="section-spacer"><div class="panel-head"><h2>Head-to-Head Recruiting Battles</h2><span>Mock board, replaceable with extracted data</span></div>{recruiting_table()}</section>
  <div class="cards-3 section-spacer">
    <article class="panel"><span class="kicker">Commonwealth Recruiting War</span><h2>State control is a pitch</h2><p>The winner gets a week of highlight clips and scoreboard confidence for every Virginia target.</p></article>
    <article class="panel"><span class="kicker">Flip Watch</span><h2>Receivers are listening</h2><p>Woodside's award week gives Virginia Tech an easy pitch to wideouts and quarterbacks.</p></article>
    <article class="panel"><span class="kicker">Pipeline Watch</span><h2>Tidewater and NOVA</h2><p>Both staffs are circling the same high-volume regions. Rivalry week can tilt the tone.</p></article>
  </div>
"""))
write(SITE / "wire" / "index.html", simple_page("Dynasty Wire", "Dynasty Wire", "News, previews, rumor blurbs, and rivalry-week media noise.", '<div class="feed-grid">' + "".join(article_card(a, 1) for a in articles) + "</div>" + '<div class="section-spacer">' + module_grid() + '</div>'))
write(SITE / "clash" / "index.html", simple_page("Commonwealth Clash", "Commonwealth Clash", "The Week 13 preview center for #10 Virginia at #6 Virginia Tech.", f"""
  <div class="preview-grid">
    <article><span>Matchup</span><strong>#10 Virginia at #6 Virginia Tech</strong><p>Top-10 CFP rivalry game in Blacksburg.</p></article>
    <article><span>Stakes</span><strong>ACC title race, CFP positioning, state bragging rights</strong><p>Every result changes the family group chat.</p></article>
    <article><span>QB Matchup</span><strong>Mike Vick Jr. vs Devante Sampson</strong><p>Heisman noise against bye-week preparation.</p></article>
    <article><span>Key Player</span><strong>Marquis Woodside</strong><p>Virginia's first question is how to cap the explosive plays.</p></article>
    <article><span>What VT Needs</span><strong>Make Virginia chase</strong><p>Early tempo and explosive passes can erase the bye advantage.</p></article>
    <article><span>What UVA Needs</span><strong>Turn it into a fourth-quarter game</strong><p>Possessions, Sanders touches, and red-zone finishing.</p></article>
    <article><span>Prediction</span><strong>Virginia Tech -4.5</strong><p>Commonwealth Wire projects Hokies 34, Cavaliers 27.</p></article>
    <article><span>X-Factor</span><strong>First turnover</strong><p>A short field could flip the rivalry script immediately.</p></article>
  </div>
  <div class="section-spacer">{article_card(articles[1], 1, "wide")}</div>
"""))
write(SITE / "records" / "index.html", simple_page("Record Watch", "Records", "A growing record book for the dynasty hub.", """
  <div class="cards-3">
    <article class="panel record-card"><strong>4</strong><span>Marquis Woodside receiving touchdowns vs Wake Forest</span></article>
    <article class="panel record-card"><strong>190</strong><span>Marquis Woodside receiving yards vs Wake Forest</span></article>
    <article class="panel record-card"><strong>44</strong><span>Mike Vick Jr. passing touchdowns through Week 12</span></article>
  </div>
"""))
for article in articles:
    write(SITE / "articles" / article["slug"] / "index.html", article_page(article))

(DATA / "articles.json").write_text(json.dumps(articles, indent=2))

print(f"Built {len(articles)} articles and static pages in {SITE}")
