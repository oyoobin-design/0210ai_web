import json, re, csv

with open('ai-tools-data.js', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'const aiToolsData = (\[[\s\S]*?\]);', content)
if not match:
    print('ERROR: Could not parse')
    exit(1)

json_str = match.group(1)
data = json.loads(json_str)

with open('AI_도구_통합_정리_2026_최종_NEW.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['대분류','카테고리','서브카테고리','툴 이름','킬러 기능','특징','비용','가입 방식','무료 한도','한국어 지원','URL'])
    for t in data:
        writer.writerow([
            t.get('major',''),
            t.get('category',''),
            t.get('subcategory',''),
            t.get('name',''),
            t.get('killer_feature',''),
            t.get('description',''),
            t.get('pricing',''),
            t.get('signup',''),
            t.get('free_tier',''),
            t.get('korean_support',''),
            t.get('url','')
        ])

print(f'Done! {len(data)} rows written.')
