# encoding=utf-8

import os

prjpath = os.getcwd()

pageDict = {
    'common':prjpath+'/logic/common.py',
    'Manage':prjpath+'/logic/Manage.py',
    'PkgManage':prjpath+'/logic/PkgManage.py'
}

actionsDict = {
    'Suggest-Manage':'common:homeEnterManage',
    'Suggest-Rank':'common:homeEnterRank',
    'Suggest-Mine':'common:homeEnterMine',
    'Rank-Suggest':'common:homeEnterSuggest',
    'Rank-Manage':'common:homeEnterManage',
    'Rank-Mine':'common:homeEnterMine',
    'Manage-Suggest':'common:homeEnterSuggest',
    'Manage-Rank':'common:homeEnterRank',
    'Manage-Mine':'common:homeEnterMine',
    'Mine-Suggest':'common:homeEnterSuggest',
    'Mine-Rank':'common:homeEnterRank',
    'Mine-Manage':'common:homeEnterManage',
    'Manage-PkgManage':'Manage:mgrEnterPkgmgr',
    'PkgManage-Manage':'PkgManage:PkgmgrEnterMgr'
}
















