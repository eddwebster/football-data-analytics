"""Module containing functions to fetch URLs for badges and logos

Functions
---------
get_competition_logo(competition)
    Get URL of competition logo for competition of choice, and format image ready for printing

get_team_badge_and_colour(team, hoa='home' )
    Get team colourmap and get URL of badge image for team of choice, and format image ready for printing.
"""

from PIL import Image
import requests
from io import BytesIO
import matplotlib.cm as cm


def get_competition_logo(competition):
    """ Get URL of competition logo for competition of choice, and format image ready for printing.

    Function to return the image PIL object for the competition of choice. The function ensures that images are
    consistently sized, and adds padding (of user defined colour) where appropriate.

    Args:
        competition (string):  competition logo to obtain.

    Returns:
        PIL Image: Formatted competition badge image.
    """

    # Initialise returns
    url = None

    if competition in ['EPL', 'Premier League', 'GB1']:
        url = "https://www.fifplay.com/img/public/premier-league-2-logo.png"

    if competition in ['EFLC', 'EFL Championship', 'Championship', 'GB2']:
        url = "https://brandlogos.net/wp-content/uploads/2022/07/efl_championship-logo_brandlogos.net_e58ej.png"

    if competition in ['La Liga', 'La_Liga', 'La Liga Santander', 'ES1']:
        url = "https://assets.laliga.com/assets/logos/laliga-v/laliga-v-1200x1200.png"

    if competition in ['Bundesliga', 'Fußball-Bundesliga', 'Fußball Bundesliga', '1 Bundesliga', '1. Bundesliga', 'L1']:
        url = "https://upload.wikimedia.org/wikipedia/en/thumb/d/df/Bundesliga_logo_%282017%29.svg/255px-Bundesliga_logo_%282017%29.svg.png"

    if competition in ['Serie A', 'Serie_A', 'Serie A TIM', 'Lega Serie A', 'IT1']:
        url = "https://1000logos.net/wp-content/uploads/2021/10/Italian-Serie-A-logo.png"

    if competition in ['Ligue 1', 'Ligue_1', 'Ligue 1 Uber Eats', 'FR1']:
        url = "https://sportivka.net/wp-content/uploads/2021/10/Ligue_1_logo_PNG1.png"

    # Get image, and resize
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = img.crop(img.getbbox())
    width, height = img.size

    if width > height:
        result = Image.new('RGBA', (width, width), color=(255, 0, 0, 0))
        result.paste(img, (0, (width - height) // 2))
    elif height > width:
        result = Image.new('RGBA', (height, height), color=(255, 0, 0, 0))
        result.paste(img, ((height - width) // 2, 0))
    else:
        result = img

    result = result.resize((300, 300))

    return result


def get_team_badge_and_colour(team, hoa='home'):
    """ Get team colourmap and get URL of badge image for team of choice, and format image ready for printing.

    Function to return the image PIL object and matplotlib colourmap for the team of choice. The function ensures
    that images are consistently sized, and adds padding (of user defined colour) where appropriate.

    Args:
        team (string): team badge and colour to obtain.
        hoa (string, optional): Selection of home or away colour. Default is 'home'.

    Returns:
        PIL Image: Formatted team badge image.
        matplotlib colormap: Matplotlib colormap object.
    """

    # Initialise returns
    url = None
    cmap = None

    if team in ['Arsenal', 'Arsenal FC']:
        url = "https://logos-world.net/wp-content/uploads/2020/05/Arsenal-Logo.png"
        cmap = cm.get_cmap('Reds') if hoa == 'home' else cm.get_cmap('Blues')

    if team in ['AC Milan', 'A.C. Milan']:
        url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Logo_of_AC_Milan.svg/195px-Logo_of_AC_Milan.svg.png"

    if team in ['Aston Villa', 'Aston Villa FC', 'Villa']:
        url = "https://upload.wikimedia.org/wikipedia/en/thumb/f/f9/Aston_Villa_FC_crest_%282016%29.svg/800px-Aston_Villa_FC_crest_%282016%29.svg.png"

    if team in ['Athletico Madrid', 'Atlético de Madrid']:
        url = "https://logos-world.net/wp-content/uploads/2020/06/atletico-madrid-Logo-700x394.png"

    if team in ['Barcelona', 'FC Barcelona']:
        url = "https://logos-world.net/wp-content/uploads/2020/04/Barcelona-Logo-700x394.png"

    if team in ['Birmingham', 'Birmingham FC', 'Birmingham City', 'Birmingham City FC']:
        url = "https://upload.wikimedia.org/wikipedia/en/thumb/6/68/Birmingham_City_FC_logo.svg/302px-Birmingham_City_FC_logo.svg.png"

    if team in ['Blackburn', 'Blackburn Rovers', 'Blackburn FC', 'Blackburn Rovers FC']:
        url = "https://seeklogo.com/images/B/blackburn-rovers-logo-410B37A022-seeklogo.com.png"

    if team in ['Blackpool', 'Blackpool FC']:
        url = "https://seeklogo.com/images/B/blackpool-fc-logo-9897552227-seeklogo.com.png"

    if team in ['Bournemouth', 'AFC Bournemouth']:
        url = "https://1000logos.net/wp-content/uploads/2018/06/AFC-Bournemouth-Logo-768x432.png"
        cmap = cm.get_cmap('Reds') if hoa == 'home' else cm.get_cmap('Blues')

    if team in ['Brentford', 'Brentford FC']:
        url = "https://images.racingpost.com/football/teambadges/378.png"

    if team in ['Brighton & Hove Albion', 'Brighton']:
        url = "https://1000logos.net/wp-content/uploads/2018/06/Brighton-Hove-Albion-Logo-768x432.png"

    if team in ['Bristol City', 'Bristol']:
        url = "https://upload.wikimedia.org/wikipedia/en/thumb/f/f5/Bristol_City_crest.svg/480px-Bristol_City_crest.svg.png"
        cmap = cm.get_cmap('Reds') if hoa == 'home' else cm.get_cmap('gray')

    if team in ['Burnley FC', 'Burnley']:
        url = "https://upload.wikimedia.org/wikipedia/en/thumb/6/62/Burnley_F.C._Logo.svg/225px-Burnley_F.C._Logo.svg.png"

    if team in ['Cadiz', 'Cadiz CF', 'Cádiz CF', 'Cádiz']:
        url = "https://upload.wikimedia.org/wikipedia/en/thumb/5/58/C%C3%A1diz_CF_logo.svg/180px-C%C3%A1diz_CF_logo.svg.png"

    if team in ['Cardiff City', 'Cardiff', 'Cardiff FC', 'Cardiff City FC']:
        url = "https://upload.wikimedia.org/wikipedia/en/thumb/3/3c/Cardiff_City_crest.svg/800px-Cardiff_City_crest.svg.png"

    if team in ['Chelsea', 'Chelsea FC']:
        url = "https://logos-world.net/wp-content/uploads/2020/05/Chelsea-Logo.png"

    if team in ['Coventry', 'Coventry City', 'Coventry FC', 'Coventry City FC']:
        url = "https://ssl.gstatic.com/onebox/media/sports/logos/KHpmY4tIwqiutl8Cfl0MAw_96x96.png"
        cmap = cm.get_cmap('Blues') if hoa == 'home' else cm.get_cmap('BuPu')

    if team in ['Crystal Palace', 'Crystal Palace FC']:
        url = "https://upload.wikimedia.org/wikipedia/hif/c/c1/Crystal_Palace_FC_logo.png"
        cmap = cm.get_cmap('Reds') if hoa == 'home' else cm.get_cmap('Blues')

    if team in ['Eintracht Frankfurt']:
        url = "https://assets-sports.thescore.com/soccer/team/115/logo.png"

    if team in ['Everton', 'Everton FC']:
        url = "https://logos-world.net/wp-content/uploads/2020/06/Everton-Logo-700x394.png"
        cmap = cm.get_cmap('Blues') if hoa == 'home' else cm.get_cmap('RdPu')

    if team in ['Fiorentina', 'ACF Fiorentina']:
        url = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/2022_ACF_Fiorentina_logo.svg/240px-2022_ACF_Fiorentina_logo.svg.png"

    if team in ['Fulham', 'Fulham FC']:
        url = "https://sportslogohistory.com/wp-content/uploads/2020/11/fulham_fc_2001-pres.png"

    if team in ['Huddersfield Town', 'Huddersfield Town FC', 'Huddersfield']:
        url = "https://upload.wikimedia.org/wikipedia/en/7/7d/Huddersfield_Town_A.F.C._logo.png"

    if team in ['Hull', 'Hull City FC', 'Hull City']:
        url = "https://upload.wikimedia.org/wikipedia/en/thumb/5/54/Hull_City_A.F.C._logo.svg/379px-Hull_City_A.F.C._logo.svg.png"
        cmap = cm.get_cmap('Oranges') if hoa == 'home' else cm.get_cmap('gray')

    if team in ['Ibiza', 'Unión Deportiva Ibiza', 'UD Ibiza']:
        url = "https://upload.wikimedia.org/wikipedia/en/thumb/a/a8/Shield_of_UD_Ibiza.png/285px-Shield_of_UD_Ibiza.png"

    if team in ['Inter', 'Inter Milan', 'FC Internazionale Milano']:
        url = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/FC_Internazionale_Milano_2021.svg/270px-FC_Internazionale_Milano_2021.svg.png"

    if team in ['Leeds', 'Leeds United', 'Leeds United FC', 'Leeds Utd']:
        url = "https://logos-world.net/wp-content/uploads/2020/06/Leeds-United-Logo-700x394.png"
        cmap = cm.get_cmap('YlOrBr') if hoa == 'home' else cm.get_cmap('Blues')

    if team in ['Luton Town', 'Luton', 'Luton Town FC']:
        url = "https://a.espncdn.com/combiner/i?img=/i/teamlogos/soccer/500/301.png"
        cmap = cm.get_cmap('Oranges') if hoa == 'home' else cm.get_cmap('gray')

    if team in ['Leicester City', 'Leicester City FC', 'Leicester']:
        url = "https://1000logos.net/wp-content/uploads/2018/06/Leicester-City-Logo.png"
        cmap = cm.get_cmap('Blues') if hoa == 'home' else cm.get_cmap('gray')

    if team in ['Levante', 'Levante UD']:
        url = "https://upload.wikimedia.org/wikipedia/en/thumb/7/7b/Levante_Uni%C3%B3n_Deportiva%2C_S.A.D._logo.svg/225px-Levante_Uni%C3%B3n_Deportiva%2C_S.A.D._logo.svg.png"

    if team in ['Liverpool', 'Liverpool FC']:
        url = "https://logos-world.net/wp-content/uploads/2020/06/Liverpool-Logo.png"
        cmap = cm.get_cmap('Reds') if hoa == 'home' else cm.get_cmap('BuPu')

    if team in ['Manchester City', 'Manchester City FC', 'Man City']:
        url = "https://logos-world.net/wp-content/uploads/2020/06/Manchester-City-Logo.png"
        cmap = cm.get_cmap('Blues') if hoa == 'home' else cm.get_cmap('gray')

    if team in ['Manchester United', 'Manchester United FC', 'Man United', 'Man Utd', 'Manchested Utd']:
        url = "https://logos-world.net/wp-content/uploads/2020/06/Manchester-United-logo-700x394.png"
        cmap = cm.get_cmap('Reds') if hoa == 'home' else cm.get_cmap('gray')

    if team in ['Middlesbrough', 'Middlesbrough FC']:
        url = "https://images.webapi.gc.middlesbroughfcservices.co.uk/fit-in/200x200/7af04870-d2d4-11ec-93d3-b732dfcf0a3b.png"

    if team in ['Millwall', 'Millwall FC']:
        url = "https://www.millwallfc.co.uk/logo.png"
        cmap = cm.get_cmap('Blues') if hoa == 'home' else cm.get_cmap('gray')

    if team in ['Newcastle United', 'Newcastle United FC', 'Newcastle', 'Newcastle Utd']:
        url = "https://logos-world.net/wp-content/uploads/2020/06/Newcastle-Logo-700x394.png"
        cmap = cm.get_cmap('gray') if hoa == 'home' else cm.get_cmap('Blues')

    if team in ['Norwich', 'Norwich FC', 'Norwich City', 'Norwich City FC']:
        url = "https://assets.stickpng.com/images/580b57fcd9996e24bc43c4e9.png"

    if team in ['Nottingham Forest', 'Nottingham Forest FC', 'Notts Forest']:
        url = "https://upload.wikimedia.org/wikipedia/commons/6/61/Nottingham_Forest_logo.png"

    if team in ['Olympique Marseille', 'Marseille', 'OM']:
        url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/Olympique_Marseille_logo.svg/255px-Olympique_Marseille_logo.svg.png"

    if team in ['Osasuna', 'CA Osasuna']:
        url = "https://upload.wikimedia.org/wikipedia/en/thumb/d/db/Osasuna_logo.svg/210px-Osasuna_logo.svg.png"

    if team in ['Paris Saint-Germain F.C.', 'Paris Saint-Germain', 'PSG']:
        url = "https://logos-world.net/wp-content/uploads/2020/06/PSG-Logo.png"

    if team in ['Preston', 'Preston North End', 'Preston FC', 'Preston North End FC', 'PNE', 'PNE FC']:
        url = "https://upload.wikimedia.org/wikipedia/en/thumb/8/82/Preston_North_End_FC.svg/300px-Preston_North_End_FC.svg.png"

    if team in ['Queens Park Rangers', 'Queens Park Rangers FC', 'QPR']:
        url = "https://cdn.bleacherreport.net/images/team_logos/328x328/queens_park_rangers.png"
        cmap = cm.get_cmap('Blues') if hoa == 'home' else cm.get_cmap('BuPu')

    if team in ['Rayo Vallecano', 'Rayo Vallecano de Madrid']:
        url = "https://seeklogo.com/images/R/Rayo_Vallecano-logo-83EC841FE5-seeklogo.com.png"

    if team in ['Reading', 'Reading FC']:
        url = "https://upload.wikimedia.org/wikipedia/en/thumb/1/11/Reading_FC.svg/270px-Reading_FC.svg.png"

    if team in ['Real Betis', 'Real Betis Balompié']:
        url = "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Real_betis_logo.svg/300px-Real_betis_logo.svg.png"

    if team in ['Real Madrid', 'Real Madrid CF']:
        url = "https://seeklogo.com/images/R/real-madrid-c-f-logo-C08F61D801-seeklogo.com.png"

    if team in ['Real Sociedad', 'Real Sociedad SAC', 'Real Sociedad S.A.C']:
        url = "https://logos-world.net/wp-content/uploads/2020/11/Real-Sociedad-Logo.png"

    if team in ['Real Valladolid', 'Real Valladolid CF']:
        url = "https://seeklogo.com/images/R/Real_Valladolid_Club_de_Futbol-logo-E2828971A8-seeklogo.com.png"

    if team in ['RBL', 'Red Bull Leipzig', 'RB Leipzig', 'RasenBallsport Leipzig']:
        url = "https://tickets.rbleipzig.com/light_custom/lightTheme/RBLogo_Shop06.png"

    if team in ['Rotherham', 'Rotherham United', 'Rotherham FC', 'Rotherham Utd', 'Rotherham United FC']:
        url = "https://upload.wikimedia.org/wikipedia/en/thumb/c/c0/Rotherham_United_FC.svg/210px-Rotherham_United_FC.svg.png"

    if team in ['AS Saint-Étienne', 'Saint-Etienne', 'Saint-Étienne']:
        url = "https://upload.wikimedia.org/wikipedia/en/thumb/2/25/AS_Saint-%C3%89tienne_logo.svg/225px-AS_Saint-%C3%89tienne_logo.svg.png"

    if team in ['Sevilla', 'Sevilla FC']:
        url = "https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Sevilla_FC_logo.svg/225px-Sevilla_FC_logo.svg.png"

    if team in ['Sheffield United', 'Sheffield United FC', 'Sheffield Utd', 'Sheff Utd']:
        url = "https://www.sufc.co.uk/logo.png"

    if team in ['Southampton', 'Southampton FC']:
        url = "https://1000logos.net/wp-content/uploads/2018/07/Southampton-Logo-640x400.png"

    if team in ['Stoke City', 'Stoke City FC', 'Stoke', 'Stoke FC']:
        url = "https://upload.wikimedia.org/wikipedia/en/thumb/2/29/Stoke_City_FC.svg/415px-Stoke_City_FC.svg.png"

    if team in ['Sunderland', 'Sunderland FC', 'Sunderland AFC']:
        url = "https://upload.wikimedia.org/wikipedia/en/thumb/7/77/Logo_Sunderland.svg/922px-Logo_Sunderland.svg.png"

    if team in ['Strasbourg', 'RC Strasbourg Alsace FC', 'RC Strasbourg']:
        url = "https://upload.wikimedia.org/wikipedia/en/thumb/8/80/Racing_Club_de_Strasbourg_logo.svg/255px-Racing_Club_de_Strasbourg_logo.svg.png"

    if team in ['Swansea City', 'Swansea City FC', 'Swansea']:
        url = "https://logos-download.com/wp-content/uploads/2016/05/Swansea_City_AFC_logo_logotype_crest.png"
        cmap = cm.get_cmap('gray') if hoa == 'home' else cm.get_cmap('Reds')

    if team in ['Tottenham Hotspur', 'Tottenham Hotspur FC', 'Tottenham', 'Spurs']:
        url = "https://logos-world.net/wp-content/uploads/2020/06/Tottenham-Hotspur-Logo-700x394.png"

    if team in ['Watford', 'Watford FC']:
        url = "https://upload.wikimedia.org/wikipedia/en/thumb/e/e2/Watford.svg/687px-Watford.svg.png"

    if team in ['Valencia', 'Valencia CF']:
        url = "https://upload.wikimedia.org/wikipedia/en/thumb/c/ce/Valenciacf.svg/240px-Valenciacf.svg.png"

    if team in ['Villarreal', 'Villarreal CF']:
        url = "https://cdn.soccerwiki.org/images/logos/clubs/174.png"

    if team in ['West Bromich Albion', 'West Bromich Albion FC', 'West Brom']:
        url = "https://upload.wikimedia.org/wikipedia/en/thumb/8/8b/West_Bromwich_Albion.svg/289px-West_Bromwich_Albion.svg.png"

    if team in ['West Ham United', 'West Ham United FC', 'West Ham', 'West Ham Utd']:
        url = "https://logos-world.net/wp-content/uploads/2020/06/West-Ham-Logo.png"
        cmap = cm.get_cmap('BuPu') if hoa == 'home' else cm.get_cmap('Blues')

    if team in ['Wigan', 'Wigan Athletic', 'Wigan FC', 'Wigan Athletic FC']:
        url = "https://upload.wikimedia.org/wikipedia/en/thumb/4/43/Wigan_Athletic.svg/800px-Wigan_Athletic.svg.png"

    if team in ['Wolverhampton Wanderers', 'Wolverhampton Wanderers FC', 'Wolves']:
        url = "https://logos-download.com/wp-content/uploads/2018/09/FC_Wolverhampton_Wanderers_Logo-700x606.png"
        cmap = cm.get_cmap('YlOrBr') if hoa == 'home' else cm.get_cmap('YlGnBu')

    # Get image, and resize
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = img.crop(img.getbbox())
    width, height = img.size

    if width > height:
        result = Image.new('RGBA', (width, width), color=(255, 0, 0, 0))
        result.paste(img, (0, (width - height) // 2))
    elif height > width:
        result = Image.new('RGBA', (height, height), color=(255, 0, 0, 0))
        result.paste(img, ((height - width) // 2, 0))
    else:
        result = img

    result = result.resize((300, 300))

    return result, cmap


