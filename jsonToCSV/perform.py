import json
import csv

input_file = './jsonToCSV/jlpt.json'

# JSON 파일 읽기
with open(input_file, 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

# 문자열 필드 정리 함수 (특수문자 제거)
def clean_string(value):
    if isinstance(value, str):
        return value.replace('\n', '').replace('\t', '')
    return value

def clean_data(obj):
    if isinstance(obj, dict):
        return {k: clean_data(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [clean_data(item) for item in obj]
    else:
        return clean_string(obj)

data = clean_data(data)

# words.csv 컬럼 정의
words_fields = [
    'word_id', 
    'link',
    'word_class',
    'star_count',
    'kanji',
    'furigana',
    'word_meaning',
    'level',
    'sentences'  # JSON 문자열로 저장
]

with open('words.csv', 'w', newline='', encoding='utf-8-sig') as words_file:
    words_writer = csv.DictWriter(words_file, fieldnames=words_fields, delimiter='@', quotechar='"', quoting=csv.QUOTE_ALL)
    words_writer.writeheader()

    for item in data:
        # word_meaning이 리스트이면 공백으로 join
        if 'word_meaning' in item and isinstance(item['word_meaning'], list):
            meaning_str = ' '.join(item['word_meaning'])
        else:
            meaning_str = item.get('word_meaning', '')

        # sentences를 JSON 문자열로 변환
        sentences_json = json.dumps(item.get('sentences', []), ensure_ascii=False)

        # 각 단어 데이터 작성
        words_row = {
            'word_id': item.get('word_id', ''),
            'link': item.get('link', ''),
            'word_class': item.get('word_class', ''),
            'star_count': item.get('star_count', ''),
            'kanji': item.get('kanji', ''),
            'furigana': item.get('furigana', ''),
            'word_meaning': meaning_str,
            'level': item.get('level', ''),
            'sentences': sentences_json  # JSON 문자열
        }
        words_writer.writerow(words_row)

print("words.csv 생성 완료!")
