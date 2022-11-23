# republish demo/cellcalc

```sql
SELECT
  payload.cellcalc.b_vol_diff as b_vol_diff,
  payload.cellcalc.b_vol_mean as b_vol_mean,
  payload.cellcalc.b_vol_std as b_vol_std,
  payload.cellcalc.b_vol_variation as b_vol_variation,
  payload.ts as tstp

FROM

  "demo/cellcalc"
```

**Action Handler**  
**action:** republish  
**target topic:** demo/cellcalc  
**payload template:**  
```
{ "vol_variation": ${b_vol_variation}, "vol_std": ${b_vol_std}, "vol_mean": ${b_vol_mean}, "vol_diff": ${b_vol_diff} } 
```
  
# republish demo/exception
```sql
SELECT

  payload as msg

FROM

  "demo/exception"
```
**Action Handler**  
**action:** republish  
**target topic:** demo/exception  
**payload template:**  
```
{ "value": "${msg}" } 
```

# republish demo/calc
```sql
SELECT

  payload.bcstd.open_vol_arr[1] as open_vol,
  payload.bcstd.work_vol_arr[1] as work_vol

FROM

  "demo/calc" 
```
**Action Handler**  
**action:** republish  
**target topic:** demo/calc   
**payload template:**  
```
{ "work_vol": ${work_vol}, "open_vol": ${open_vol} }
```
   
