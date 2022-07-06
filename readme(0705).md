# 📗마크다운

- 2004년 존 그루버가 만든 텍스트 기반의 갑벼운 마크업 언어
- 최초 마크다운에 비해 확장된 문법(표, 주석) 존재

## ✔ 마크다운의 특징
- 워드 프로세서(한글/MS word)는 다양한 서식과 구조를 지원하며, 문서에 즉각적으로 반영
- 마크다운은 가능한 읽을 수 있도록 최소한의 문법으로 구조화(make it as readable as possible)
- 마크다운은 단순 텍스트 문법으로 내용을 작성하며, 다양한 환경에서 변환하여 보여짐
    - 다양한 text editor, 웹 환경에서 모두 지원

## ✔ 마크다운 문법
- Heading은 문서의 제목이나 소제목으로 사용
    - #의 개수에 따라 대응되는 수준(Heading level)이 있으며, h1~h6까지 표현 가능
        - #1개는 h1, #6개는 h6
    - 문서의 구조를 위해 작성되며 글자 크기를 조절하기 위해 사용되어서는 안 됨
- List는 순서가 있는 리스트(ol)와 순서가 없는 리스트(ul)로 구성
    - 순서가 있는 리스트(ol)
        1. First item
        2. Second item
        3. Third item
    - 순서가 없는 리스트(ul)
        - First item
        - Second item
        - Third item
- 코드 블럭은 backtick 기호 3개를 활용하여 작성, 코드 블록에 특정 언어를 명시하면 Syntax Highlighting 적용 가능
    - 단, 일부 환경에서는 적용이 되지 않을 수 있음
    ```
    {
        "firstName": "John",
        "lastName": "Smith",
        "age" : 25
    }
    ```
- 코드 블록은 backtick 기호 1개를 인라인에 활용하여 작성
    - At the command prompt, type `nano`
- Link는 [문자열]'(url)을 통해 링크 작성 가능, ctrl+click 으로 해당 링크 클릭 시 이동 가능, 이미지도 연결 가능
- 인용문은 > 를 통해 작성
> Dorothy followed her through many of the beautiful rooms in her castle.
- 표는 | 를 통해 작성

| Syntax | Description |
| ------ | ----------- |
| Header | Title |
|Paragraph | Text |

- text 강조
    - 굵게(Bold) ** 두개
        - **굵은 글씨**
    - 기울임(Italic) *한개
        - *기울인 글씨*
    - 굵고 기울임(Bold + Italic) *** 3개
        - ***굵고 기울인 글씨***

- Markdown editer
    - Typora
    - visual code
    