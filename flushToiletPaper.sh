function removeTrashFiles {
    CLEAR=$1
    if [ $1 != "home" ]; then
       cd ./${CLEAR}
    fi
    rm -rf *.4ct
    rm -rf *.4tc
    rm -rf *.aux
    rm -rf *.auxlock
    rm -rf *.dvi
    rm -rf *.html
    rm -rf *.ids
    rm -rf *.ids
    rm -rf *.idv
    rm -rf *.jax
    rm -rf *.lg
    rm -rf *.log
    rm -rf *.oc
    rm -rf *.toc
    rm -rf *.pdf
    rm -rf *.out
    rm -rf *.sage
    rm -rf *.sagetex.sage
    rm -rf *.sagetex.sage.py
    rm -rf *.sagetex.scmd
    rm -rf *.sagetex.sout
    rm -rf *.tmp
    rm -rf *.xref
    if [ $1 != "home" ]; then
       cd ../
    fi
}

removeTrashFiles "home"
removeTrashFiles "module1Activity"
removeTrashFiles "module2Activity"
removeTrashFiles "module3Activity"
removeTrashFiles "module4Activity"
removeTrashFiles "module5Activity"
removeTrashFiles "module6Activity"
removeTrashFiles "module7Activity"
removeTrashFiles "module8Activity"
removeTrashFiles "module9LimitsActivity"
removeTrashFiles "module10LimitsActivity"
removeTrashFiles "module11LimitsActivity"
removeTrashFiles "module12LimitsActivity"
removeTrashFiles "module9ModelingActivity"
removeTrashFiles "module10ModelingActivity"
removeTrashFiles "module11ModelingActivity"
removeTrashFiles "module12ModelingActivity"
