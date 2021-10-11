import { Component, EventEmitter, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-piaui',
  templateUrl: './piaui.component.html',
  styleUrls: ['./piaui.component.css']
})
export class PiauiComponent implements OnInit {

  @Output() clickedLocal = new EventEmitter;

  constructor() { }

  ngOnInit(): void {}

  getLocal(event) {
    this.clickedLocal.emit(event);
  }

}
