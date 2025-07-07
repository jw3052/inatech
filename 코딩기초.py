import pandas as pd

학생정보 = pd.DataFrame({
    "이름": ["지희", "소연", "윤희", "하진", "효선"],
    "성별": ["여","남","남","여","여"],
    "국어": [78, 88, 92, 90, 80],
    "수학": [90, 89, 86, 87, 92]
})

학생정보.to_excel("학생정보.xlsx", index=False)

불러온정보 = pd.read_excel("학생정보.xlsx")
print(불러온정보)