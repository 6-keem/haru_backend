import json
import csv

input_file = 'jlpt.json'

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
    'sentence_id'  # 대표 문장 ID
]

# sentence.csv 컬럼 정의
sentence_fields = [
    'sentence_id',
    'kr',
    'jp'
]

with open('words.csv', 'w', newline='', encoding='utf-8-sig') as words_file, \
     open('sentence.csv', 'w', newline='', encoding='utf-8-sig') as sentence_file:
    
    words_writer = csv.DictWriter(words_file, fieldnames=words_fields, delimiter='@')
    sentence_writer = csv.DictWriter(sentence_file, fieldnames=sentence_fields, delimiter='@')
    
    words_writer.writeheader()
    sentence_writer.writeheader()

    sentence_id_counter = 1

    for item in data:
        # word_meaning이 리스트이면 공백으로 join
        if 'word_meaning' in item and isinstance(item['word_meaning'], list):
            meaning_str = ' '.join(item['word_meaning'])
        else:
            meaning_str = item.get('word_meaning', '')

        sentences = item.get('sentences', [])
        
        representative_sentence_id = ''
        for i, s in enumerate(sentences):
            kr = s.get('kr', '')
            jp = s.get('jp', '')

            current_sentence_id = sentence_id_counter
            sentence_id_counter += 1

            # 첫 번째 문장을 대표 sentence_id로 사용
            if i == 0:
                representative_sentence_id = current_sentence_id

            sentence_row = {
                'sentence_id': current_sentence_id,
                'kr': kr,
                'jp': jp
            }
            sentence_writer.writerow(sentence_row)

        words_row = {
            'word_id': item.get('word_id', ''),
            'link': item.get('link', ''),
            'word_class': item.get('word_class', ''),
            'star_count': item.get('star_count', ''),
            'kanji': item.get('kanji', ''),
            'furigana': item.get('furigana', ''),
            'word_meaning': meaning_str,
            'level': item.get('level', ''),
            'sentence_id': representative_sentence_id
        }
        words_writer.writerow(words_row)

print("words.csv, sentence.csv 생성 완료!")
