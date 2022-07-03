from bs4 import BeautifulSoup
import requests
cookies = {
    'djvideovol': '1',
    'wsjregion': 'na%2Cus',
    'gdprApplies': 'false',
    'ab_uuid': '910db8df-a883-44a0-acfe-2045327e8d59',
    'usr_bkt': '830nwKog3K',
    'cX_P': 'l50hn1bywyk1mr8y',
    'cX_S': 'l50hn1c15x4il3q6',
    '_sp_v1_uid': '1:653:f69f4dae-f369-46b1-9a56-1ca2693760d2',
    '_sp_v1_ss': '1:H4sIAAAAAAAAAItWqo5RKimOUbLKK83J0YlRSkVil4AlqmtrlXSoqiwWACMYp9h2AAAA',
    '_sp_v1_opt': '1:',
    '_sp_v1_csv': 'null',
    '_sp_v1_lt': '1:',
    'consentUUID': '983b7511-c048-43ce-8738-12bccf367b41',
    'cX_G': 'cx%3A364zavs26p8r3g8139a2mn1ip%3A1jc103mes1a24',
    'hok_seg': 'none',
    '_gcl_au': '1.1.1569414957.1656560987',
    'AMCVS_CB68E4BA55144CAA0A4C98A5%40AdobeOrg': '1',
    '_lc2_fpi': '7880a1137012--01g6sbnc02v3gyfw4qpj0k3j9s',
    's_cc': 'true',
    'permutive-id': '0a28385b-e642-46f2-83da-4898df82af6a',
    'djvideovol': '1',
    'optimizelyEndUserId': 'oeu1656569971156r0.8569471761874665',
    'has_optimizely': 'true',
    'ki_r': '',
    'vidoraUserId': 'd41ch1gc4b9jg214s1iap9eek91qjh',
    'djadplaynum': '2',
    'djcs_route': '3d527d8b-32b6-4c55-9f07-b9667fb9f630',
    '_ga': 'GA1.2.773229670.1656599703',
    '_gid': 'GA1.2.740173979.1656599703',
    's_vnum': '1688135500437%26vn%3D2',
    's_vmonthnum': '1656648000439%26vn%3D2',
    'djcs_secid': 'NjA2ZTAwM2MtMTRhZS00MDdkLWFjZmEtNDBiYzZjYzc3ZjIx.ISU3k1zywweIBolhrVk_yd9rtaXR7L4YHtEtTc83JgQ',
    'sub_type': 'WSJ-SUB',
    'TR': 'V2-f17d78673d9356688c41d618c44b7c8e247fc9ca022e11dbe830175807e91b3d',
    'djcs_auto': 'M1656536624%2FTSXvrUzUAuLcmJGJggDfnpol67GxmZxB4zzernbJX94el0ehWJxhnbiCn2fvrGLG87Yu0pfz9mW9GKqp4p2KxAje0OYpu6pS6K0z71pvaSMKZ%2B6yt%2FVIRjCDN%2FAG4ooYtfJaPTzQVUuKWdxAdbFqcJZgBzF5s8EP25ZQ45wLP248IA6dL1Nkuy%2FFe50RItTlsjXh2ix750bG67NXTQ3xvb2mN1JP73GffveB9M8%2BVIwV9drVnwtGu68fquV5g53ui9EnFkvJob%2FSRRzX2EDqSGvhKAGbaZ0zRt3lu9Fjq%2FbjRgO7Izuq6b4XviAgCPPrxaVJ2TJyNk%2FdMls4in977xN7xwQil537W2k0hD5etM8gMQ7JbDRNSuZdDOnhPpXPfv4XY6akO3Y0NPIrORiqHA%3D%3DG',
    'djcs_session': 'M1656600228%2FOm%2FFs6JlILz5S2PdlpxDk4%2BOLo8V2%2BwQD5q7tJriOZbuBM%2FQp3Z5bFsEZPXi%2FZ9ooU10qu20igxTodoH8Wlwnj8ZyN8A5LdTzyevyWDyCllHHfKBA7ImOsyrqUQacY1vCRQgi5iQkDCgjxbhhVsgGEAMRPrbbDlGTI%2FsvRviRSPVKDHcYgJ3SaEVbrl0DE15zVJvsAgVG5G5Rb9sSX611Jofb4KkF1Qf%2FWWY2okPfXAmDCMokSxBc7tv8gsyikZeWI5x9hMuxAdpMGiRXteIAmZbsT9zG%2Bm8BxqbgbNkWF9SsJIvoVwVRWHc%2BcIZfd8m%2FrFAz7dP9cqZOYEQ0kOA9iBez%2B4OeIbMTKg%2BHfnTIxhYep2u4cEQgodd254HQkdzrmvL3s%2BvrtVt7jo0wtpuI3uOpDNvKbfLVfB2Mj3Y5wPvwpIgDeFB9vKcUATruy2R6Vq5D1atkf3EUPCobvsN4sEBAFHkoIJw2F1cx4aKh3MFEY%2BKaIovo4q3kURzHw0fbaJki7TKkZAwY1nIv3%2F4BDcTnSr%2Ff1RF3sJasop4XBI%3DG',
    '_li_dcdm_c': '.wsj.com',
    '_am_sp_djcsses.1fc3': '*',
    'AMCV_CB68E4BA55144CAA0A4C98A5%40AdobeOrg': '1585540135%7CMCIDTS%7C19174%7CMCMID%7C07690901460270655772963594103674630553%7CMCAAMLH-1657215620%7C7%7CMCAAMB-1657215620%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1656618020s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.0',
    'DJSESSION': 'country%3Dus%7C%7Ccontinent%3D%7C%7Cregion%3D',
    '_sp_v1_data': '2:371407:1656560986:0:59:0:59:0:0:_:-1',
    #'utag_main': f"v_id:0181b2baac80000ca4f6fd567c450507500f406d00942{_sn:6$_se:2$_ss:0$_st:1656612641357$vapi_domain:wsj.com$_prevpage:WSJ_Article_C%20Suite_Studios%20Battle%20for%20Players%20of%20%E2%80%98Hypercasual%E2%80%99%20Videogames%2C%20the%20Latest%20Mobile%20Distraction%3Bexp-1656614441362$ses_id:1656610819904%3Bexp-session$_pn:2%3Bexp-session}",
    'ResponsiveConditional_initialBreakpoint': 'xs',
    'usr_prof_v2': 'eyJvcCI6eyJqIjp7fX0sImljIjo1fQ%3D%3D',
    'ccpaApplies': 'true',
    '_ncg_sp_ses.5378': '*',
    '_ncg_id_': 'cf35ae80-7b0e-4486-960f-79e617bea292',
    '_rdt_uuid': '1656610842347.8741e0ea-f979-495a-8c1f-abcc97c4c0cc',
    '_scid': '4ccba0b1-ad41-44a8-a376-44c22a106c98',
    '_ncg_g_id_': 'a70c1102-ba3b-4b3f-9784-50157f7ab387',
    '_ncg_sp_id.5378': 'cf35ae80-7b0e-4486-960f-79e617bea292.1656610842.1.1656610843.1656610842.7962ab88-0083-4c60-bf2b-827aa1a5547c',
    'outbrain_cid_fetch': 'true',
    '_derived_epik': 'dj0yJnU9V2FMcnhmOFpnZEEyYjM5a3UzSmRxTUt1WkV6RE0ta1Mmbj04RnNwckthZW9pdzJ3ODRYYzRKc0dRJm09MSZ0PUFBQUFBR0s5NEJzJnJtPTEmcnQ9QUFBQUFHSzk0QnM',
    '_pin_unauth': 'dWlkPU4yUmxaVEUzWm1RdFlqTXlNQzAwT0dFNExXSXpaV1V0WW1FNU0yUmhZV1ZsWVdGbQ',
    '_sctr': '1|1656561600000',
    'ki_t': '1656570047172%3B1656570047172%3B1656610844527%3B1%3B12',
    's_tp': '10663',
    's_ppv': 'WSJ_Article_C%2520Suite_Studios%2520Battle%2520for%2520Players%2520of%2520%25u2018Hypercasual%25u2019%2520Videogames%252C%2520the%2520Latest%2520Mobile%2520Distraction%2C75%2C58%2C8002',
    '_am_sp_djcsid.1fc3': 'd9dc2521-e8cd-4baa-a80c-6e22a4360a2a.1656560987.4.1656610862.1656602507.ad25a019-824b-47e3-a91c-155cbe5cb085',
}

headers = {
    'authority': 'www.wsj.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': f"djvideovol=1; wsjregion=na%2Cus; gdprApplies=false; ab_uuid=910db8df-a883-44a0-acfe-2045327e8d59; usr_bkt=830nwKog3K; cX_P=l50hn1bywyk1mr8y; cX_S=l50hn1c15x4il3q6; _sp_v1_uid=1:653:f69f4dae-f369-46b1-9a56-1ca2693760d2; _sp_v1_ss=1:H4sIAAAAAAAAAItWqo5RKimOUbLKK83J0YlRSkVil4AlqmtrlXSoqiwWACMYp9h2AAAA; _sp_v1_opt=1:; _sp_v1_csv=null; _sp_v1_lt=1:; consentUUID=983b7511-c048-43ce-8738-12bccf367b41; cX_G=cx%3A364zavs26p8r3g8139a2mn1ip%3A1jc103mes1a24; hok_seg=none; _gcl_au=1.1.1569414957.1656560987; AMCVS_CB68E4BA55144CAA0A4C98A5%40AdobeOrg=1; _lc2_fpi=7880a1137012--01g6sbnc02v3gyfw4qpj0k3j9s; s_cc=true; permutive-id=0a28385b-e642-46f2-83da-4898df82af6a; djvideovol=1; optimizelyEndUserId=oeu1656569971156r0.8569471761874665; has_optimizely=true; ki_r=; vidoraUserId=d41ch1gc4b9jg214s1iap9eek91qjh; djadplaynum=2; djcs_route=3d527d8b-32b6-4c55-9f07-b9667fb9f630; _ga=GA1.2.773229670.1656599703; _gid=GA1.2.740173979.1656599703; s_vnum=1688135500437%26vn%3D2; s_vmonthnum=1656648000439%26vn%3D2; djcs_secid=NjA2ZTAwM2MtMTRhZS00MDdkLWFjZmEtNDBiYzZjYzc3ZjIx.ISU3k1zywweIBolhrVk_yd9rtaXR7L4YHtEtTc83JgQ; sub_type=WSJ-SUB; TR=V2-f17d78673d9356688c41d618c44b7c8e247fc9ca022e11dbe830175807e91b3d; djcs_auto=M1656536624%2FTSXvrUzUAuLcmJGJggDfnpol67GxmZxB4zzernbJX94el0ehWJxhnbiCn2fvrGLG87Yu0pfz9mW9GKqp4p2KxAje0OYpu6pS6K0z71pvaSMKZ%2B6yt%2FVIRjCDN%2FAG4ooYtfJaPTzQVUuKWdxAdbFqcJZgBzF5s8EP25ZQ45wLP248IA6dL1Nkuy%2FFe50RItTlsjXh2ix750bG67NXTQ3xvb2mN1JP73GffveB9M8%2BVIwV9drVnwtGu68fquV5g53ui9EnFkvJob%2FSRRzX2EDqSGvhKAGbaZ0zRt3lu9Fjq%2FbjRgO7Izuq6b4XviAgCPPrxaVJ2TJyNk%2FdMls4in977xN7xwQil537W2k0hD5etM8gMQ7JbDRNSuZdDOnhPpXPfv4XY6akO3Y0NPIrORiqHA%3D%3DG; djcs_session=M1656600228%2FOm%2FFs6JlILz5S2PdlpxDk4%2BOLo8V2%2BwQD5q7tJriOZbuBM%2FQp3Z5bFsEZPXi%2FZ9ooU10qu20igxTodoH8Wlwnj8ZyN8A5LdTzyevyWDyCllHHfKBA7ImOsyrqUQacY1vCRQgi5iQkDCgjxbhhVsgGEAMRPrbbDlGTI%2FsvRviRSPVKDHcYgJ3SaEVbrl0DE15zVJvsAgVG5G5Rb9sSX611Jofb4KkF1Qf%2FWWY2okPfXAmDCMokSxBc7tv8gsyikZeWI5x9hMuxAdpMGiRXteIAmZbsT9zG%2Bm8BxqbgbNkWF9SsJIvoVwVRWHc%2BcIZfd8m%2FrFAz7dP9cqZOYEQ0kOA9iBez%2B4OeIbMTKg%2BHfnTIxhYep2u4cEQgodd254HQkdzrmvL3s%2BvrtVt7jo0wtpuI3uOpDNvKbfLVfB2Mj3Y5wPvwpIgDeFB9vKcUATruy2R6Vq5D1atkf3EUPCobvsN4sEBAFHkoIJw2F1cx4aKh3MFEY%2BKaIovo4q3kURzHw0fbaJki7TKkZAwY1nIv3%2F4BDcTnSr%2Ff1RF3sJasop4XBI%3DG; _li_dcdm_c=.wsj.com; _am_sp_djcsses.1fc3=*; AMCV_CB68E4BA55144CAA0A4C98A5%40AdobeOrg=1585540135%7CMCIDTS%7C19174%7CMCMID%7C07690901460270655772963594103674630553%7CMCAAMLH-1657215620%7C7%7CMCAAMB-1657215620%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1656618020s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.0; DJSESSION=country%3Dus%7C%7Ccontinent%3D%7C%7Cregion%3D; _sp_v1_data=2:371407:1656560986:0:59:0:59:0:0:_:-1; utag_main=v_id:0181b2baac80000ca4f6fd567c450507500f406d00942{_sn:6$_se:2$_ss:0$_st:1656612641357$vapi_domain:wsj.com$_prevpage:WSJ_Article_C%20Suite_Studios%20Battle%20for%20Players%20of%20%E2%80%98Hypercasual%E2%80%99%20Videogames%2C%20the%20Latest%20Mobile%20Distraction%3Bexp-1656614441362$ses_id:1656610819904%3Bexp-session$_pn:2%3Bexp-session;} ResponsiveConditional_initialBreakpoint=xs; usr_prof_v2=eyJvcCI6eyJqIjp7fX0sImljIjo1fQ%3D%3D; ccpaApplies=true; _ncg_sp_ses.5378=*; _ncg_id_=cf35ae80-7b0e-4486-960f-79e617bea292; _rdt_uuid=1656610842347.8741e0ea-f979-495a-8c1f-abcc97c4c0cc; _scid=4ccba0b1-ad41-44a8-a376-44c22a106c98; _ncg_g_id_=a70c1102-ba3b-4b3f-9784-50157f7ab387; _ncg_sp_id.5378=cf35ae80-7b0e-4486-960f-79e617bea292.1656610842.1.1656610843.1656610842.7962ab88-0083-4c60-bf2b-827aa1a5547c; outbrain_cid_fetch=true; _derived_epik=dj0yJnU9V2FMcnhmOFpnZEEyYjM5a3UzSmRxTUt1WkV6RE0ta1Mmbj04RnNwckthZW9pdzJ3ODRYYzRKc0dRJm09MSZ0PUFBQUFBR0s5NEJzJnJtPTEmcnQ9QUFBQUFHSzk0QnM; _pin_unauth=dWlkPU4yUmxaVEUzWm1RdFlqTXlNQzAwT0dFNExXSXpaV1V0WW1FNU0yUmhZV1ZsWVdGbQ; _sctr=1|1656561600000; ki_t=1656570047172%3B1656570047172%3B1656610844527%3B1%3B12; s_tp=10663; s_ppv=WSJ_Article_C%2520Suite_Studios%2520Battle%2520for%2520Players%2520of%2520%25u2018Hypercasual%25u2019%2520Videogames%252C%2520the%2520Latest%2520Mobile%2520Distraction%2C75%2C58%2C8002; _am_sp_djcsid.1fc3=d9dc2521-e8cd-4baa-a80c-6e22a4360a2a.1656560987.4.1656610862.1656602507.ad25a019-824b-47e3-a91c-155cbe5cb085",
    'referer': 'https://www.wsj.com/search?query=cryptocurrency&isToggleOn=true&operator=AND&sort=date-desc&duration=1y&startDate=2010%2F05%2F14&endDate=2022%2F06%2F28&source=wsjie%2Cblog%2Cwsjvideo%2Cinteractivemedia%2Cwsjsitesrch%2Cwsjpro%2Cwsjaudio',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}

params = {
    'page': '1',
}

pages = 4
urls=[]
count = 0
for page in range(1, pages+1):
    url = 'https://www.wsj.com/search?query=cryptocurrency&isToggleOn=true&operator=AND&sort=date-desc&duration=1y&startDate=2010%2F05%2F14&endDate=2022%2F06%2F28&source=wsjie%2Cblog%2Cwsjvideo%2Cinteractivemedia%2Cwsjsitesrch%2Cwsjpro%2Cwsjaudio&page=27' + str(count)
    count = count + 1
    res = requests.get(url.format(page), headers={"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"})
    soup = BeautifulSoup(res.text, "lxml")
    for item in soup.select('.WSJTheme--headline--7VCzo7Ay '):
       # headline = item.find('h2').get_text()
        _href = item.find('a')['href']
        urls.append(_href)
num = 0
for _href in urls:
    num = num + 1
    if num == 26:
        break
    lines_to_append = []
    try:
        resp = requests.get(_href, params=params, cookies=cookies, headers=headers)
    except Exception as e:
        try:
            resp = requests.get("https://www.wsj.com" + _href)
        except Exception as e:
            continue
    sauce = BeautifulSoup(resp.text, "lxml")
    for para in sauce.find_all("p"):
        lines_to_append.append(para.get_text())

    with open('output'+str(num) + '.txt', "a+") as file_object:
        appendEOL = False
        # Move read cursor to the start of file.
        file_object.seek(0)
        # Check if file is not empty
        data = file_object.read(100)
        if len(data) > 0:
            appendEOL = True
        # Iterate over each string in the list

        file_object.write('Article' + str(num))
        for line in lines_to_append:
            # If file is not empty then append '\n' before first line for
            # other lines always append '\n' before appending line
            if appendEOL == True:
                file_object.write("\n")
            else:
                appendEOL = True
            # Append element at the end of file
            file_object.write(line)
