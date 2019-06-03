# encoding=utf-8
import os

prjpath = os.getcwd()

pageDict = {'common':prjpath+'/logic/common.py',
            'Manage':prjpath+'/logic/Manage.py',
            'PkgManage':prjpath+'/logic/PkgManage.py'
}

actionsDict = {'Suggest-Manage':'common:homeEnterManage',
               'Suggest-Rank':'common:homeEnterRank',
               'Rank-Suggest':'common:homeEnterSuggest',
               'Rank-Manage':'common:homeEnterManage',
               'Manage-Suggest':'common:homeEnterSuggest',
               'Manage-Rank':'common:homeEnterRank',
               'Manage-PkgManage':'Manage:mgrEnterPkgmgr',
               'PkgManage-Manage':'PkgManage:pkgmgrEnterMgr',
               'Suggest-Mine':'common:homeEnterMine',
               'Manage-Mine':'common:homeEnterMine',
               'Rank-Mine':'common:homeEnterMine',
               'Mine-Suggest':'common:homeEnterSuggest',
               'Mine-Manage':'common:homeEnterManage',
               'Mine-Rank':'common:homeEnterRank'
}









