MsgBox "Se ha detectado una amenaza por favor apaga el sistema",48,"FATAL ERROR 404"
speaks="Se ha detectado una amenaza por favor apaga el sistema"
Set speech=CreateObject("sapi.spvoice")
speech.Speak speaks
