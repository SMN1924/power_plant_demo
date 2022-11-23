# exception detection
**Rule ID**:exception detection  
**SQL**:
```sql
select airc1->ac_vol as ac_vol ,cast(ts,"datetime") as utctime from dt1Stream where airc1->ac_vol > 235;
```
**Actions(Sink):** mqtt  
**MQTT broker address:** tcp://emqx:1883   
**MQTT topic:** demo/exception  
**send single:** true  
**Data template:** 
```
{{.utctime}}, AC1 Voltage warning, Current voltage:{{.ac_vol}}V.  
```
# battery cellcalc
**Rule ID**:battery cellcalc  
**SQL**:
```sql
select cellcalc(*),ts as ts from dt1Stream;
```
**Actions(Sink):** mqtt  
**MQTT broker address:** tcp://emqx:1883   
**MQTT topic:** demo/cellcalc  
**send single:** true 

# battery calc
**Rule ID**:battery calc  
**SQL**:
```sql
select bcstd(*) from dt1Stream;
```
**Actions(Sink):** mqtt  
**MQTT broker address:** tcp://emqx:1883   
**MQTT topic:** demo/calc  
**send single:** true    

# filter
**Rule ID**:filter  
**SQL**:
```sql
select * from dt1Stream GROUP BY `type`,TUMBLINGWINDOW(ss, 10);
```
**Actions(Sink):** mqtt  
**MQTT broker address:** tcp://emqx:1883   
**MQTT topic:** demo/filter   
**send single:** true  

# data transfer
**Rule ID**:data transfer  
**SQL**:
```sql
select * from neuronStream;
```
**Actions(Sink):** memory     
**topic:** data_transfer  
**send single:** true  
**Data template:** 
```
{
    "type":"CONT",
    "ts":{{.timestamp | int64}},
    "dess1":{
        "bm1":{
            "j6":{
                "elec":{
                    "work_vol":{{divf .values.tag117 100}},
                    "temptiny":{{divf .values.tag118 100}},
                    "open_vol":{{divf .values.tag119 100}},
                    "stat":{{divf .values.tag120 100}}
                },
                "ebtu":{
                    "vol16":{{divf .values.tag116 100}},
                    "vol15":{{divf .values.tag115 100}},
                    "vol14":{{divf .values.tag114 100}},
                    "vol13":{{divf .values.tag113 100}},
                    "vol12":{{divf .values.tag112 100}},
                    "vol11":{{divf .values.tag111 100}},
                    "vol10":{{divf .values.tag110 100}},
                    "vol09":{{divf .values.tag109 100}},
                    "vol08":{{divf .values.tag108 100}},
                    "vol07":{{divf .values.tag107 100}},
                    "vol06":{{divf .values.tag106 100}},
                    "vol05":{{divf .values.tag105 100}},
                    "vol04":{{divf .values.tag104 100}},
                    "vol03":{{divf .values.tag103 100}},
                    "vol02":{{divf .values.tag102 100}},
                    "vol01":{{divf .values.tag101 100}}
                }
            },
            "j5":{
                "elec":{
                    "work_vol":{{divf .values.tag97 100}},
                    "temptiny":{{divf .values.tag98 100}},
                    "open_vol":{{divf .values.tag99 100}},
                    "stat":{{divf .values.tag100 100}}
                },
                "ebtu":{
                    "vol16":{{divf .values.tag96 100}},
                    "vol15":{{divf .values.tag95 100}},
                    "vol14":{{divf .values.tag94 100}},
                    "vol13":{{divf .values.tag93 100}},
                    "vol12":{{divf .values.tag92 100}},
                    "vol11":{{divf .values.tag91 100}},
                    "vol10":{{divf .values.tag90 100}},
                    "vol09":{{divf .values.tag89 100}},
                    "vol08":{{divf .values.tag88 100}},
                    "vol07":{{divf .values.tag87 100}},
                    "vol06":{{divf .values.tag86 100}},
                    "vol05":{{divf .values.tag85 100}},
                    "vol04":{{divf .values.tag84 100}},
                    "vol03":{{divf .values.tag83 100}},
                    "vol02":{{divf .values.tag82 100}},
                    "vol01":{{divf .values.tag81 100}}
                }
            },
            "j4":{
                "elec":{
                    "work_vol":{{divf .values.tag77 100}},
                    "temptiny":{{divf .values.tag78 100}},
                    "open_vol":{{divf .values.tag79 100}},
                    "stat":{{divf .values.tag80 100}}
                },
                "ebtu":{
                    "vol16":{{divf .values.tag76 100}},
                    "vol15":{{divf .values.tag75 100}},
                    "vol14":{{divf .values.tag74 100}},
                    "vol13":{{divf .values.tag73 100}},
                    "vol12":{{divf .values.tag72 100}},
                    "vol11":{{divf .values.tag71 100}},
                    "vol10":{{divf .values.tag70 100}},
                    "vol09":{{divf .values.tag69 100}},
                    "vol08":{{divf .values.tag68 100}},
                    "vol07":{{divf .values.tag67 100}},
                    "vol06":{{divf .values.tag66 100}},
                    "vol05":{{divf .values.tag65 100}},
                    "vol04":{{divf .values.tag64 100}},
                    "vol03":{{divf .values.tag63 100}},
                    "vol02":{{divf .values.tag62 100}},
                    "vol01":{{divf .values.tag61 100}}
                }
            },
            "j3":{
                "elec":{
                    "work_vol":{{divf .values.tag57 100}},
                    "temptiny":{{divf .values.tag58 100}},
                    "open_vol":{{divf .values.tag59 100}},
                    "stat":{{divf .values.tag60 100}}
                },
                "ebtu":{
                    "vol16":{{divf .values.tag56 100}},
                    "vol15":{{divf .values.tag55 100}},
                    "vol14":{{divf .values.tag54 100}},
                    "vol13":{{divf .values.tag53 100}},
                    "vol12":{{divf .values.tag52 100}},
                    "vol11":{{divf .values.tag51 100}},
                    "vol10":{{divf .values.tag50 100}},
                    "vol09":{{divf .values.tag49 100}},
                    "vol08":{{divf .values.tag48 100}},
                    "vol07":{{divf .values.tag47 100}},
                    "vol06":{{divf .values.tag46 100}},
                    "vol05":{{divf .values.tag45 100}},
                    "vol04":{{divf .values.tag44 100}},
                    "vol03":{{divf .values.tag43 100}},
                    "vol02":{{divf .values.tag42 100}},
                    "vol01":{{divf .values.tag41 100}}
                }
            },
            "j2":{
                "elec":{
                    "work_vol":{{divf .values.tag37 100}},
                    "temptiny":{{divf .values.tag38 100}},
                    "open_vol":{{divf .values.tag39 100}},
                    "stat":{{divf .values.tag40 100}}
                },
                "ebtu":{
                    "vol16":{{divf .values.tag36 100}},
                    "vol15":{{divf .values.tag35 100}},
                    "vol14":{{divf .values.tag34 100}},
                    "vol13":{{divf .values.tag33 100}},
                    "vol12":{{divf .values.tag32 100}},
                    "vol11":{{divf .values.tag31 100}},
                    "vol10":{{divf .values.tag30 100}},
                    "vol09":{{divf .values.tag29 100}},
                    "vol08":{{divf .values.tag28 100}},
                    "vol07":{{divf .values.tag27 100}},
                    "vol06":{{divf .values.tag26 100}},
                    "vol05":{{divf .values.tag25 100}},
                    "vol04":{{divf .values.tag24 100}},
                    "vol03":{{divf .values.tag23 100}},
                    "vol02":{{divf .values.tag22 100}},
                    "vol01":{{divf .values.tag21 100}}
                }
            },
            "j1":{
                "elec":{
                    "work_vol":{{divf .values.tag17 100}},
                    "temptiny":{{divf .values.tag18 100}},
                    "open_vol":{{divf .values.tag19 100}},
                    "stat":{{divf .values.tag20 100}}
                },
                "ebtu":{
                    "vol16":{{divf .values.tag16 100}},
                    "vol15":{{divf .values.tag15 100}},
                    "vol14":{{divf .values.tag14 100}},
                    "vol13":{{divf .values.tag13 100}},
                    "vol12":{{divf .values.tag12 100}},
                    "vol11":{{divf .values.tag11 100}},
                    "vol10":{{divf .values.tag10 100}},
                    "vol09":{{divf .values.tag9 100}},
                    "vol08":{{divf .values.tag8 100}},
                    "vol07":{{divf .values.tag7 100}},
                    "vol06":{{divf .values.tag6 100}},
                    "vol05":{{divf .values.tag5 100}},
                    "vol04":{{divf .values.tag4 100}},
                    "vol03":{{divf .values.tag3 100}},
                    "vol02":{{divf .values.tag2 100}},
                    "vol01":{{divf .values.tag1 100}}
                }
            }
        }
    },
    "airc1":{
      "recirculated_temp":{{.values.tag121}},
      "outside_temp":{{.values.tag122}},
      "humidity":{{.values.tag123}},
      "device_stat":{{.values.tag124}},
      "ac_vol": {{.values.tag125}},
      "temp_set":{{.values.tag126}},
      "ac_ov_set":{{.values.tag127}},
      "ac_lv_set":{{.values.tag128}},
      "ac_ov_alert":{{.values.tag129}},
      "ac_lv_alert":{{.values.tag130}}
    },
  "airc2":{
    "recirculated_temp":{{.values.tag131}},
    "outside_temp":{{.values.tag132}},
    "humidity":{{.values.tag133}},
    "device_stat":{{.values.tag134}},
    "ac_vol": {{.values.tag135}},
    "temp_set":{{.values.tag136}},
    "ac_ov_set":{{.values.tag137}},
    "ac_lv_set":{{.values.tag138}},
    "ac_ov_alert":{{.values.tag139}},
    "ac_lv_alert":{{.values.tag140}}
  }
} 
```
**Actions(Sink):** mqtt  
**MQTT broker address:** tcp://emqx:1883   
**MQTT topic:** demo/transfer   
**send single:** true  
**Data template:** 
```
{
    "type":"CONT",
    "ts":{{.timestamp | int64}},
    "dess1":{
        "bm1":{
            "j6":{
                "elec":{
                    "work_vol":{{divf .values.tag117 100}},
                    "temptiny":{{divf .values.tag118 100}},
                    "open_vol":{{divf .values.tag119 100}},
                    "stat":{{divf .values.tag120 100}}
                },
                "ebtu":{
                    "vol16":{{divf .values.tag116 100}},
                    "vol15":{{divf .values.tag115 100}},
                    "vol14":{{divf .values.tag114 100}},
                    "vol13":{{divf .values.tag113 100}},
                    "vol12":{{divf .values.tag112 100}},
                    "vol11":{{divf .values.tag111 100}},
                    "vol10":{{divf .values.tag110 100}},
                    "vol09":{{divf .values.tag109 100}},
                    "vol08":{{divf .values.tag108 100}},
                    "vol07":{{divf .values.tag107 100}},
                    "vol06":{{divf .values.tag106 100}},
                    "vol05":{{divf .values.tag105 100}},
                    "vol04":{{divf .values.tag104 100}},
                    "vol03":{{divf .values.tag103 100}},
                    "vol02":{{divf .values.tag102 100}},
                    "vol01":{{divf .values.tag101 100}}
                }
            },
            "j5":{
                "elec":{
                    "work_vol":{{divf .values.tag97 100}},
                    "temptiny":{{divf .values.tag98 100}},
                    "open_vol":{{divf .values.tag99 100}},
                    "stat":{{divf .values.tag100 100}}
                },
                "ebtu":{
                    "vol16":{{divf .values.tag96 100}},
                    "vol15":{{divf .values.tag95 100}},
                    "vol14":{{divf .values.tag94 100}},
                    "vol13":{{divf .values.tag93 100}},
                    "vol12":{{divf .values.tag92 100}},
                    "vol11":{{divf .values.tag91 100}},
                    "vol10":{{divf .values.tag90 100}},
                    "vol09":{{divf .values.tag89 100}},
                    "vol08":{{divf .values.tag88 100}},
                    "vol07":{{divf .values.tag87 100}},
                    "vol06":{{divf .values.tag86 100}},
                    "vol05":{{divf .values.tag85 100}},
                    "vol04":{{divf .values.tag84 100}},
                    "vol03":{{divf .values.tag83 100}},
                    "vol02":{{divf .values.tag82 100}},
                    "vol01":{{divf .values.tag81 100}}
                }
            },
            "j4":{
                "elec":{
                    "work_vol":{{divf .values.tag77 100}},
                    "temptiny":{{divf .values.tag78 100}},
                    "open_vol":{{divf .values.tag79 100}},
                    "stat":{{divf .values.tag80 100}}
                },
                "ebtu":{
                    "vol16":{{divf .values.tag76 100}},
                    "vol15":{{divf .values.tag75 100}},
                    "vol14":{{divf .values.tag74 100}},
                    "vol13":{{divf .values.tag73 100}},
                    "vol12":{{divf .values.tag72 100}},
                    "vol11":{{divf .values.tag71 100}},
                    "vol10":{{divf .values.tag70 100}},
                    "vol09":{{divf .values.tag69 100}},
                    "vol08":{{divf .values.tag68 100}},
                    "vol07":{{divf .values.tag67 100}},
                    "vol06":{{divf .values.tag66 100}},
                    "vol05":{{divf .values.tag65 100}},
                    "vol04":{{divf .values.tag64 100}},
                    "vol03":{{divf .values.tag63 100}},
                    "vol02":{{divf .values.tag62 100}},
                    "vol01":{{divf .values.tag61 100}}
                }
            },
            "j3":{
                "elec":{
                    "work_vol":{{divf .values.tag57 100}},
                    "temptiny":{{divf .values.tag58 100}},
                    "open_vol":{{divf .values.tag59 100}},
                    "stat":{{divf .values.tag60 100}}
                },
                "ebtu":{
                    "vol16":{{divf .values.tag56 100}},
                    "vol15":{{divf .values.tag55 100}},
                    "vol14":{{divf .values.tag54 100}},
                    "vol13":{{divf .values.tag53 100}},
                    "vol12":{{divf .values.tag52 100}},
                    "vol11":{{divf .values.tag51 100}},
                    "vol10":{{divf .values.tag50 100}},
                    "vol09":{{divf .values.tag49 100}},
                    "vol08":{{divf .values.tag48 100}},
                    "vol07":{{divf .values.tag47 100}},
                    "vol06":{{divf .values.tag46 100}},
                    "vol05":{{divf .values.tag45 100}},
                    "vol04":{{divf .values.tag44 100}},
                    "vol03":{{divf .values.tag43 100}},
                    "vol02":{{divf .values.tag42 100}},
                    "vol01":{{divf .values.tag41 100}}
                }
            },
            "j2":{
                "elec":{
                    "work_vol":{{divf .values.tag37 100}},
                    "temptiny":{{divf .values.tag38 100}},
                    "open_vol":{{divf .values.tag39 100}},
                    "stat":{{divf .values.tag40 100}}
                },
                "ebtu":{
                    "vol16":{{divf .values.tag36 100}},
                    "vol15":{{divf .values.tag35 100}},
                    "vol14":{{divf .values.tag34 100}},
                    "vol13":{{divf .values.tag33 100}},
                    "vol12":{{divf .values.tag32 100}},
                    "vol11":{{divf .values.tag31 100}},
                    "vol10":{{divf .values.tag30 100}},
                    "vol09":{{divf .values.tag29 100}},
                    "vol08":{{divf .values.tag28 100}},
                    "vol07":{{divf .values.tag27 100}},
                    "vol06":{{divf .values.tag26 100}},
                    "vol05":{{divf .values.tag25 100}},
                    "vol04":{{divf .values.tag24 100}},
                    "vol03":{{divf .values.tag23 100}},
                    "vol02":{{divf .values.tag22 100}},
                    "vol01":{{divf .values.tag21 100}}
                }
            },
            "j1":{
                "elec":{
                    "work_vol":{{divf .values.tag17 100}},
                    "temptiny":{{divf .values.tag18 100}},
                    "open_vol":{{divf .values.tag19 100}},
                    "stat":{{divf .values.tag20 100}}
                },
                "ebtu":{
                    "vol16":{{divf .values.tag16 100}},
                    "vol15":{{divf .values.tag15 100}},
                    "vol14":{{divf .values.tag14 100}},
                    "vol13":{{divf .values.tag13 100}},
                    "vol12":{{divf .values.tag12 100}},
                    "vol11":{{divf .values.tag11 100}},
                    "vol10":{{divf .values.tag10 100}},
                    "vol09":{{divf .values.tag9 100}},
                    "vol08":{{divf .values.tag8 100}},
                    "vol07":{{divf .values.tag7 100}},
                    "vol06":{{divf .values.tag6 100}},
                    "vol05":{{divf .values.tag5 100}},
                    "vol04":{{divf .values.tag4 100}},
                    "vol03":{{divf .values.tag3 100}},
                    "vol02":{{divf .values.tag2 100}},
                    "vol01":{{divf .values.tag1 100}}
                }
            }
        }
    },
    "airc1":{
      "recirculated_temp":{{.values.tag121}},
      "outside_temp":{{.values.tag122}},
      "humidity":{{.values.tag123}},
      "device_stat":{{.values.tag124}},
      "ac_vol": {{.values.tag125}},
      "temp_set":{{.values.tag126}},
      "ac_ov_set":{{.values.tag127}},
      "ac_lv_set":{{.values.tag128}},
      "ac_ov_alert":{{.values.tag129}},
      "ac_lv_alert":{{.values.tag130}}
    },
  "airc2":{
    "recirculated_temp":{{.values.tag131}},
    "outside_temp":{{.values.tag132}},
    "humidity":{{.values.tag133}},
    "device_stat":{{.values.tag134}},
    "ac_vol": {{.values.tag135}},
    "temp_set":{{.values.tag136}},
    "ac_ov_set":{{.values.tag137}},
    "ac_lv_set":{{.values.tag138}},
    "ac_ov_alert":{{.values.tag139}},
    "ac_lv_alert":{{.values.tag140}}
  }
} 
```


