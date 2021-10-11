import { Component, EventEmitter, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-bahia',
  templateUrl: './bahia.component.html',
  styleUrls: ['./bahia.component.css']
})
export class BahiaComponent implements OnInit {

  @Output() clickedLocal = new EventEmitter;

  constructor() { }

  ngOnInit(): void {}

  getLocal(event) {
    this.clickedLocal.emit(event);
  }

}
