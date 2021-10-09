import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PernambucoComponent } from './pernambuco.component';

describe('PernambucoComponent', () => {
  let component: PernambucoComponent;
  let fixture: ComponentFixture<PernambucoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PernambucoComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PernambucoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
