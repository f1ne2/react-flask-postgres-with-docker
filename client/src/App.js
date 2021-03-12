import React from 'react';
import Q from './img/Q.jpg';
import student_using_laptop from
      './img/student_using_laptop.png';
import ball from "./img/ball.png"
import greenball from "./img/ball2.png"
import pinkball from "./img/ball3.png"
import Api from './component/Api'


const items = [
    {id: 1, title: 'Разработка на Python'},
    {id: 2, title: 'Веб-разработка'},
    {id: 3, title: 'Тестирование ПО'},
    {id: 4, title: 'Разработка на Java'},
    {id: 5, title: 'Интернет-маркетинг'},
    {id: 6, title: 'Android-разработка'},
    {id: 7, title: 'Графический дизайн'},
    {id: 8, title: 'Искусственный интеллект'},
    {id: 9, title: 'Информационная безопасность'},
    {id: 10, title: 'Frontend-разработка'}]




function App() {
  return (
      <div className="table table-borderless">
          <table width="100%"  align="center">
              <tr>
                  <td colSpan="2">
                      <div className="circle"></div>
                  </td>
              </tr>
              <tr>
                  <td rowSpan="3">
                      <div className="circle2"></div>
                  </td>
                  <td height="50%">
                      <p>TAKE
                          <span>THE</span>
                          <img src={Q} className="img-fluid"/>UIZZZ!
                      </p>
                      <p className="select"> Select category:</p>
                  </td>
                  <td colSpan="2">
                      <img src={student_using_laptop} className="img-fluid student" />
                  </td>
              </tr>
              <tr>
                  <td>
                      <div className="category"> {items[0].title} </div>
                  </td>
                  <td>
                      <div className="category"> {items[1].title} </div>
                  </td>
                  <td>
                    <div className="category"> {items[2].title}</div>
                  </td>
              </tr>
              <tr>
                  <td>
                      <div className="category"> {items[3].title}</div>
                  </td>
                  <td>
                      <div className="category"> {items[4].title}</div>
                  </td>
                  <td>
                      <div className="category"> {items[5].title}</div>
                  </td>
              </tr>
              <tr>
                  <td></td>
                  <td>
                      <div className="category"> {items[6].title}</div>
                  </td>
                  <td>
                      <div className="category"> {items[7].title}</div>
                  </td>
                  <td>
                      <div className="category"> {items[8].title}</div>
                  </td>
              </tr>
              <tr>
                  <td></td>
                  <td>
                      <div className="category"> {items[9].title}</div>
                  </td>
              </tr>
          </table>
          <table width="100%" align="center">
              <tr>
                  <td>
                      <div className="container greenball">
                          <img src={greenball} className="img-fluid"/>
                      </div>
                  </td>
              </tr>
              <tr>
                  <td>
                      <div className="container purpleball">
                      <img src={ball} className="img-fluid"/>
                      </div>
                  </td>
              </tr>
              <tr>
                  <td>
                      <div className="container pinkball">
                          <img src={pinkball} className="img-fluid"/>
                      </div>
                  </td>
              </tr>
          </table>
          <Api />
            </div>
  );
}

export default App;
