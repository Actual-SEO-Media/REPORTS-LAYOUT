        import pandas as pd
        import numpy as np
        import server_RK as srk
        from pyodide import create_proxy
        GHR = 'Google HOU Rank'
        KW = 'Keyword'
        VSBY = 'Visibility'
        GHD = 'Google HOU Difference'
        GP = 'Google Previous'
        GMHR = 'Google Mobile HOU Rank'
        KW = 'Keyword'
        VSBY = 'Visibility'
        GMHD = 'Google Mobile HOU Difference'
        GMP = 'Google Mobile HOU Previous'
        BNGR = 'Bing US Rank'
        KW = 'Keyword'
        VSBY = 'Visibility'
        BNGDF = "Bing US Difference"
        BNGP = 'Bing US Previous'
        YAHR = 'Yahoo! Rank'
        KW = 'Keyword'
        VSBY = 'Visibility'
        YAHDIF = "Yahoo! Difference"
        YAHP = 'Yahoo! Previous'
        SE = "SE"
        NOTE = "NOTE"
        GMHR = 'Google Mobile HOU Rank'
        GMHD = 'Google Mobile HOU Difference'
        RP = 'Ranking pages'
        REPORT_NAME = ['Google Report', 'Google Mobile Report', 'Bing Report', 'Yahoo! Report']
        COLUMN_NAME = ['Keyword', 'Ranking pages', 'Google HOU Rank', 'Google Previous', 'Google HOU Difference', 'NOTE']
        frame_data = srk.FIND_FRAME("ABBA_TEST.csv")
        GOD = frame_data[0]
        GOD_NAME = REPORT_NAME[0]
        for i in range(len(frame_data[0])):
         CHILD = document.createElement("tr")
         CHILD.style.fontFamily = "SFPROREG"
         CHILD.style.position = "relative"
         CHILD.style.top = "-50px"
         CHILD.style.background = "white"



         parent = document.querySelector("#ROWS")
         parent.appendChild(CHILD)
         for r in range(6):
          LAST_CHILD = document.createElement("td")
          DF_GOD = pd.DataFrame(data=GOD)
          LAST_CHILD.style.fontFamily = "SFPROREG"

          LAST_CHILD.innerHTML = DF_GOD[COLUMN_NAME[r]][i]
          CHILD.appendChild(LAST_CHILD)
          
            import pandas as pd
        import numpy as np
        import server_RK as srk
        from pyodide import create_proxy
        GHR = 'Google HOU Rank'
        KW = 'Keyword'
        VSBY = 'Visibility'
        GHD = 'Google HOU Difference'
        GP = 'Google Previous'
        GMHR = 'Google Mobile HOU Rank'
        KW = 'Keyword'
        VSBY = 'Visibility'
        GMHD = 'Google Mobile HOU Difference'
        GMP = 'Google Mobile HOU Previous'
        BNGR = 'Bing US Rank'
        KW = 'Keyword'
        VSBY = 'Visibility'
        BNGDF = "Bing US Difference"
        BNGP = 'Bing US Previous'
        YAHR = 'Yahoo! Rank'
        KW = 'Keyword'
        VSBY = 'Visibility'
        YAHDIF = "Yahoo! Difference"
        YAHP = 'Yahoo! Previous'
        SE = "SE"
        NOTE = "NOTE"
        GMHR = 'Google Mobile HOU Rank'
        GMHD = 'Google Mobile HOU Difference'
        RP = 'Ranking pages'
        REPORT_NAME = ['Google Report', 'Google Mobile Report', 'Bing Report', 'Yahoo! Report']
        COLUMN_NAME = ['Keyword', 'Ranking pages', GMHR, GMP , GMHD, 'NOTE']
        frame_data = srk.FIND_FRAME("ABBA_TEST.csv")
        GOM = frame_data[1]
        GOM_NAME = REPORT_NAME[1]
        for i in range(len(frame_data[1])):
         CHILD = document.createElement("tr")
         CHILD.style.fontFamily = "SFPROREG"
         CHILD.style.position = "relative"
         CHILD.style.top = "-50px"
         CHILD.style.background = "white"
         parent = document.querySelector("#ROWS1")
         parent.appendChild(CHILD)
         
         for r in range(6):
          LAST_CHILD = document.createElement("td")
          DF_GOM = pd.DataFrame(data=GOM)
          LAST_CHILD.style.fontFamily = "SFPROREG"
    
          LAST_CHILD.innerHTML = DF_GOM[COLUMN_NAME[r]][i]
          CHILD.appendChild(LAST_CHILD)
          
        
        
            import pandas as pd
                                                    import numpy as np
                                                    import server_RK as srk
                                                    from pyodide import create_proxy
                                                    GHR = 'Google HOU Rank'
                                                    KW = 'Keyword'
                                                    VSBY = 'Visibility'
                                                    GHD = 'Google HOU Difference'
                                                    GP = 'Google Previous'
                                                    GMHR = 'Google Mobile HOU Rank'
                                                    KW = 'Keyword'
                                                    VSBY = 'Visibility'
                                                    GMHD = 'Google Mobile HOU Difference'
                                                    GMP = 'Google Mobile HOU Previous'
                                                    BNGR = 'Bing US Rank'
                                                    KW = 'Keyword'
                                                    VSBY = 'Visibility'
                                                    BNGDF = "Bing US Difference"
                                                    BNGP = 'Bing US Previous'
                                                    YAHR = 'Yahoo! Rank'
                                                    KW = 'Keyword'
                                                    VSBY = 'Visibility'
                                                    YAHDIF = "Yahoo! Difference"
                                                    YAHP = 'Yahoo! Previous'
                                                    SE = "SE"
                                                    NOTE = "NOTE"
                                                    GMHR = 'Google Mobile HOU Rank'
                                                    GMHD = 'Google Mobile HOU Difference'
                                                    RP = 'Ranking pages'
                                                    REPORT_NAME = ['Google Report', 'Google Mobile Report', 'Bing Report', 'Yahoo! Report']
                                                    COLUMN_NAME = ['Keyword', 'Ranking pages', 'Google HOU Rank', 'Google Previous', 'Google HOU Difference', 'NOTE']
                                                    frame_data = srk.FIND_FRAME("ABBA_TEST.csv")
                                                    GOD = frame_data[0]
                                                    GOD_NAME = REPORT_NAME[0]
                                                    KEY_PARENT = Element("KEY_WORD")
                                                    KEY_PARENT.clear()
                                                    KEY_PARENT.element.innerHTML = str(len(GOD))
                                                     
                                                    import pandas as pd
    import numpy as np
    import server_RK as srk
    from pyodide import create_proxy
    GHR = 'Google HOU Rank'
    KW = 'Keyword'
    VSBY = 'Visibility'
    GHD = 'Google HOU Difference'
    GP = 'Google Previous'
    GMHR = 'Google Mobile HOU Rank'
    KW = 'Keyword'
    VSBY = 'Visibility'
    GMHD = 'Google Mobile HOU Difference'
    GMP = 'Google Mobile HOU Previous'
    BNGR = 'Bing US Rank'
    KW = 'Keyword'
    VSBY = 'Visibility'
    BNGDF = "Bing US Difference"
    BNGP = 'Bing US Previous'
    YAHR = 'Yahoo! Rank'
    KW = 'Keyword'
    VSBY = 'Visibility'
    YAHDIF = "Yahoo! Difference"
    YAHP = 'Yahoo! Previous'
    SE = "SE"
    NOTE = "NOTE"
    GMHR = 'Google Mobile HOU Rank'
    GMHD = 'Google Mobile HOU Difference'
    RP = 'Ranking pages'
    REPORT_NAME = ['Google Report', 'Google Mobile Report', 'Bing Report', 'Yahoo! Report']
    COLUMN_NAME = ['Keyword', 'Ranking pages', BNGR, BNGP, BNGDF, 'NOTE']
    frame_data = srk.FIND_FRAME("ABBA_TEST.csv")
    BNG = frame_data[2]
    BNG_NAME = REPORT_NAME[2]
    for i in range(len(frame_data[2])):
     CHILD = document.createElement("tr")
     CHILD.style.fontFamily = "SFPROREG"
     CHILD.style.position = "relative"
     CHILD.style.top = "-50px"
     CHILD.style.background = "white"
     parent = document.querySelector("#ROWS2")
     parent.appendChild(CHILD)
     for r in range(6):
      LAST_CHILD = document.createElement("td")
      DF_BNG = pd.DataFrame(data=BNG)
      LAST_CHILD.style.fontFamily = "SFPROREG"

      LAST_CHILD.innerHTML = DF_BNG[COLUMN_NAME[r]][i]
      CHILD.appendChild(LAST_CHILD)
      
        import pandas as pd
    import numpy as np
    import server_RK as srk
    from pyodide import create_proxy
    GHR = 'Google HOU Rank'
    KW = 'Keyword'
    VSBY = 'Visibility'
    GHD = 'Google HOU Difference'
    GP = 'Google Previous'
    GMHR = 'Google Mobile HOU Rank'
    KW = 'Keyword'
    VSBY = 'Visibility'
    GMHD = 'Google Mobile HOU Difference'
    GMP = 'Google Mobile HOU Previous'
    BNGR = 'Bing US Rank'
    KW = 'Keyword'
    VSBY = 'Visibility'
    BNGDF = "Bing US Difference"
    BNGP = 'Bing US Previous'
    YAHR = 'Yahoo! Rank'
    KW = 'Keyword'
    VSBY = 'Visibility'
    YAHDIF = "Yahoo! Difference"
    YAHP = 'Yahoo! Previous'
    SE = "SE"
    NOTE = "NOTE"
    GMHR = 'Google Mobile HOU Rank'
    GMHD = 'Google Mobile HOU Difference'
    RP = 'Ranking pages'
    REPORT_NAME = ['Google Report', 'Google Mobile Report', 'Bing Report', 'Yahoo! Report']
    COLUMN_NAME = ['Keyword', 'Ranking pages', YAHR, YAHP, YAHDIF, 'NOTE']
    frame_data = srk.FIND_FRAME("ABBA_TEST.csv")
    YAH = frame_data[3]
    YAH_NAME = REPORT_NAME[3]
    for i in range(len(frame_data[3])):
     CHILD = document.createElement("tr")
     CHILD.style.fontFamily = "SFPROREG"
     CHILD.style.position = "relative"
     CHILD.style.top = "-50px"
     CHILD.style.background = "white"
     parent = document.querySelector("#ROWS3")
     parent.appendChild(CHILD)
     for r in range(6):
      LAST_CHILD = document.createElement("td")
      DF_YAH = pd.DataFrame(data=YAH)
      LAST_CHILD.style.fontFamily = "SFPROREG"

      LAST_CHILD.innerHTML = DF_YAH[COLUMN_NAME[r]][i]
      CHILD.appendChild(LAST_CHILD)
      
    
    
    
    
        
        