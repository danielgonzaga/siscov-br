import { Component, EventEmitter, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-minas-gerais',
  templateUrl: './minas-gerais.component.html',
  styleUrls: ['./minas-gerais.component.css']
})
export class MinasGeraisComponent implements OnInit {

  @Output() clickedLocal = new EventEmitter;

  constructor() { }

  ngOnInit(): void {}

  getLocal(event) {
    this.clickedLocal.emit(event);
  }

}
