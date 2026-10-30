# ขอบเขตที่ตรวจสอบจากระบบจริง

Repository: `intasan/machine-learning-project`
ฐาน source ที่ตรวจ: `02704697da35e1011eba31f756290e6ea1e98bb4`

**สถานะ: ยังประมวลผลไม่ได้**

รัน data_cleaning.py แล้วไม่พบ data/input.csv; gesture pipeline ขาด cv2 และไม่มี dataset ที่แนบใน Repository

## แหล่งหลักฐาน

- [evidence/attempt-hand_gesture_pipeline-py.txt](../evidence/attempt-hand_gesture_pipeline-py.txt)
- [evidence/source-audit.json](../evidence/source-audit.json)
- [evidence/attempt-data_cleaning-py.txt](../evidence/attempt-data_cleaning-py.txt)

## Traceability จาก source

| ไฟล์ที่ตรวจ | ขอบเขตที่ยืนยันได้ |
|---|---|
| [data_cleaning.py](../data_cleaning.py) | พบ source ใน commit ข้างต้น; การมีไฟล์ไม่ใช่การทดสอบผ่าน |
| [hand_gesture_pipeline.py](../hand_gesture_pipeline.py) | พบ source ใน commit ข้างต้น; การมีไฟล์ไม่ใช่การทดสอบผ่าน |
| [motorcycle_scraper.py](../motorcycle_scraper.py) | พบ source ใน commit ข้างต้น; การมีไฟล์ไม่ใช่การทดสอบผ่าน |

## เกณฑ์ตรวจรับ BA / SA

| เกณฑ์ | หลักฐาน / สถานะ |
|---|---|
| ขอบเขตปัจจุบันตรงกับ source | ยังประมวลผลไม่ได้ |
| End-to-end ด้วยข้อมูลจริง | รัน data_cleaning.py แล้วไม่พบ data/input.csv; gesture pipeline ขาด cv2 และไม่มี dataset ที่แนบใน Repository |
| ผลการทดสอบที่ทำซ้ำได้ | อ่าน command, stdout, exit code ใน evidence; syntax check ไม่ใช่ runtime test |
| ข้อมูลจริงและ provenance | เฉพาะราคาทองใน live-verification.txt ที่มี URL/เวลา publication; ไม่ใช้ fixture เป็นข้อมูลจริง |
| UAT โดยเจ้าของงานหรือผู้ใช้งาน | ยังไม่ได้ดำเนินการในรอบนี้ |

## ข้อจำกัดการแสดงผลงาน

ผล unit tests เป็นการตรวจ logic โดยมี fixture ตาม suite เดิม ไม่ใช่หลักฐานธุรกรรมจริง การฝึกโมเดลจริง การทำงานของอุปกรณ์จริง หรือการรับรองจากผู้ใช้ ไม่สร้างข้อมูลธุรกิจทดแทนข้อมูลที่ขาด และไม่อนุมานว่าไม่มีข้อมูลเท่ากับปลอดภัย
