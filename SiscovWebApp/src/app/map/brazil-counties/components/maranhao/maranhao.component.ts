import { Component, EventEmitter, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-maranhao',
  templateUrl: './maranhao.component.html',
  styleUrls: ['./maranhao.component.css']
})
export class MaranhaoComponent implements OnInit {

  @Output() clickedLocal = new EventEmitter;

  constructor() { }

  ngOnInit(): void {}

  getLocal(event) {
    this.clickedLocal.emit(event);
  }

}
