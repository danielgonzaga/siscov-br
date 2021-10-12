import { Component, EventEmitter, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-paraiba',
  templateUrl: './paraiba.component.html',
  styleUrls: ['./paraiba.component.css']
})
export class ParaibaComponent implements OnInit {

  @Output() clickedLocal = new EventEmitter;

  constructor() { }

  ngOnInit(): void {}

  getLocal(event) {
    this.clickedLocal.emit(event);
  }

}
