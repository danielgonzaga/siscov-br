import { Component, EventEmitter, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-tocantins',
  templateUrl: './tocantins.component.html',
  styleUrls: ['./tocantins.component.css']
})
export class TocantinsComponent implements OnInit {

  @Output() clickedLocal = new EventEmitter;

  constructor() { }

  ngOnInit(): void {}

  getLocal(event) {
    this.clickedLocal.emit(event);
  }

}
