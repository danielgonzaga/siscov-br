import { Component, EventEmitter, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-pernambuco',
  templateUrl: './pernambuco.component.html',
  styleUrls: ['./pernambuco.component.css']
})
export class PernambucoComponent implements OnInit {

  @Output() clickedLocal = new EventEmitter;

  constructor() { }

  ngOnInit(): void {}

  getLocal(event) {
    this.clickedLocal.emit(event);
  }

}
