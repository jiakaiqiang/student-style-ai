import json
def main():
    user_info = {
         "name": "kai", 
         "role":"前端开发",
         "years_of_experience": 3,
         "target":"agent应用开发"
    }
    print(f"我是 {user_info.get('name')}, 我是一名{user_info.get('role')}, 我有{user_info.get('years_of_experience')}年的经验, 正在学习{user_info.get('target')}")


def test_main():
    skills = ["HTML", "CSS", "JavaScript"]

    skills.append('Python')
    
    print('python' in skills)  # 输出: True



def  json_transoport():
    learning_record = {
    "name": "Kai",
    "current_stage": "Python 基础",
    "completed": False,
    "topics": ["变量", "条件判断", "循环", "函数", "JSON"]
    }
    # 将 Python 对象转换为 JSON 字符串
    json_string = json.dumps(learning_record, ensure_ascii=False)
    print(json_string)
    print(type(json_string))  # 输出: <class 'str'>
    print(json.loads(json_string))  # 将 JSON 字符串转换回 Python 对象

if __name__ == "__main__":
    main()
    test_main()
    json_transoport()





 

  import json

  from pathlib import Path


  def save_record(record, file_path):
      with open(file_path, 'w', encoding='utf-8') as f:
          json.dump(record, f, ensure_ascii=False, indent=4)


  def load_record(file_path):
      with open(file_path, 'r', encoding='utf-8') as f:
          return json.load(f)


  def main():
      learning_record = {
          "name": "你的名字",
          "role": "frontend developer",
          "target": "Agent developer",
          "completed": False,
          "stage":"Python 阶段 2",
          "topics": ["变量", "函数", "JSON"]
      }

      data_dir = Path("data")
      data_dir.mkdir(exist_ok=True)
      file_path = data_dir / "stage_02_record.json"

      save_record(learning_record, file_path)
      loaded_record = load_record(file_path)
      print(f"当前阶段：{loaded_record['stage']}")
      print(f"学习目标：{loaded_record['target']}")


  main()