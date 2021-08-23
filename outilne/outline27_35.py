'''
27. 인증 넣기
    1.def hello_world에 인증 방식 추가
    2.타인이 수정 못하게 하기
    

28. 27-2의 함수들을 decorator을 써서 이쁘게 수정

29. media

30. 아이디가 노출되므로, 닉네임 만들기 . 즉 프로필앱 => 닉네임, 프로필사진(이미지), 메세지 으로 구성
1개의 계정(account)에는 1개의 프로필만 존재
delete, detail View는 필요없다.

form관련 설명 => 우리 형식대로 바꿔야 하니깐 Model Form이 필요하다. => 기존의 model을 form으로 변환해주는 방식


31. profileapp의 createView 구현
    accounts/detail 에서 profiles/create/ 로 갈 수 있는 통로 만들기

        def form_valid(self, form):
        temp_profile = form.save(commit=False)         #커스텀마이징하려는 내용. 괄호안의 form은 forms.py에서 날라온 데이터이며 (self, form)의 form에 저장된다.
        temp_profile.user = self.request.user            #user라는 데이터가 아직 없다. temp_profile의 user라는 데이터를 self에서 request를 보는 당사자 유저로 정해준다.
        temp_profile.save()

        return super().form_valid(form)       #기존의 함수와 똑같다. 그리고 나머지는 조상(부모클래스)의 원래 그거의 결과를 return해준다.


'''